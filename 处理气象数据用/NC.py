import numpy as np
import dask.array as da
import xarray as xr

# 以延迟打开的方式加载数据
data = xr.open_dataset('F:/数据/CN05.1_Tm_1961_2018_daily_025x025.nc', chunks={'time': 365})

# 按月标记数据
subset_data = data['tm'].sel(time=slice('2010', '2014'))
subset_data['month'] = subset_data['time.month']

# 按季节提取数据
winter_data = subset_data.sel(time=subset_data['month'].isin([1,2,3,11,12]))

# 提取坐标
x_coords = winter_data.coords['lon'].values
y_coords = winter_data.coords['lat'].values

# 创建空白数组
result = np.zeros((y_coords.size, x_coords.size), dtype=np.uint32)

# 建立重分类表
bins = np.array([-1e20, -30, -25, -20, -15, -10, -5, -2, 0, 5, 10, 1e20])
bins_chunked = da.from_array(bins, chunks=5)
new_values = np.array([1, 2, 3, 4, 5, 6, 6, 7, 4, 2, 0])
new_values_chunked = da.from_array(new_values, chunks=5)

# 循环处理每个时间步
for i in range(winter_data.time.size):
    # 提取时间步数据
    subset_data_rc = winter_data['tm'][i, :, :]

    # 应用重分类
    subset_data_rc = da.interp(subset_data_rc, bins_chunked, new_values_chunked)

    # 设定 nodata 值
    subset_data_rc = da.where(
        (subset_data_rc >= 0) & (subset_data_rc <= 7), 
        subset_data_rc, 
        255
    )

    # 累加数据到结果数组
    result += subset_data_rc.astype(np.uint32)

# 将数据输出为 TIFF 格式文件
profile = {'driver': 'GTiff', 'height': result.shape[0], 
           'width': result.shape[1], 'count': 1, 
           'dtype': 'uint8', 'crs': data.crs, 'transform': data.transform}
with rio.open('output_data.tif', 'w', **profile) as dst:
    dst.write(result.astype(np.uint8), 1)