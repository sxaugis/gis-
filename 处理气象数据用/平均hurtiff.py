import xarray as xr
import numpy as np
import rasterio

# 读取nc文件
ds = xr.open_dataset('D:\hur_day_BCC_ssp585_2015-2024_I_test.nc')

# 计算每10年的平均气温
weights = np.cos(np.deg2rad(ds.lat))
ds_weighted = ds.weighted(weights)
ds_weighted_mean = ds_weighted.mean(('lat', 'lon'))
temp = ds_weighted_mean['hur']
temp_decade = temp.groupby('time.year').mean('time').resample(year='10AS').mean()

# 将结果写入新的tiff文件
profile = ds.hur.isel(time=0).rio.profile
profile.update({'count': 1, 'dtype': 'float32'})
with rasterio.open('temp_decade_mean.tiff', 'w', **profile) as dst:
    dst.write(temp_decade.values, 1)