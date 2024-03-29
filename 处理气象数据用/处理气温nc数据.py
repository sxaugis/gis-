import xarray as xr
import pandas as pd
import numpy as np

# 打开.nc文件
data = xr.open_dataset('F:/数据/CN05.1_Tmax_1961_2018_daily_025x025.nc')
print(data)
# 获取温度变量
temp = data['tmax']

# 获取时间变量
time = data['time']

# 将时间转换为pandas的datetime类型
time = pd.to_datetime(time.values)

# 获取经度和纬度变量
lat = data['lat']
lon = data['lon']

# 获取时间起始索引和结束索引
start_idx = np.where(time == pd.Timestamp('2010-11-01'))[0][0]
end_idx = np.where(time == pd.Timestamp('2014-03-31'))[0][0]

# 获取需要的时间段

temp_filtered = temp[start_idx:end_idx+1]

# 获取11月到3月的数据
temp_filtered = temp_filtered.sel(time=temp_filtered['time.month'].isin([11, 12, 1, 2, 3]))

# 筛选超过10度的像元
temp_filtered = temp_filtered.where(temp_filtered > 10, 0)
temp_filtered = temp_filtered.where(temp_filtered <= 10, 1)
pixels_over_10 = temp_filtered.sum(dim='time')

# 定义输出文件名
output_file = 'outputtm.tif'

# 将数据集转为DataArray，并设置经度和纬度坐标
da = xr.DataArray(pixels_over_10, coords={'lat': lat, 'lon': lon}, dims=['lat', 'lon'])

# 导出为GeoTIFF格式
da.rio.to_raster(output_file, driver='GTiff', dtype='float32', crs='EPSG:4326')

