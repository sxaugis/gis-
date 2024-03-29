# import xarray as xr
# import geopandas as gpd
# import rasterio.mask

# data = xr.open_dataset('F:\\baiduunet\\0914\\hur_Amon_BCC-CSM2-MR_historical_r1i1p1f1_gn_197001-200912\\hur_Amon_BCC-CSM2-MR_historical_r1i1p1f1_gn_197001-200912.nc')
# shapefile = gpd.read_file('F:\\baiduunet\\0914\\nothern\\nothern.shp')
# geoms = shapefile.geometry.values
# masked_data, _ = rasterio.mask.mask(data['hur'].rio.write_crs(), geoms, data['hur'], invert=True)
# masked_data_dataset = xr.Dataset({'hur': (('band', 'y', 'x'), masked_data)})
# masked_data_dataset.to_netcdf('F:\\baiduunet\\0914\\hur_Amon_BCC-CSM2-MR_historical_r1i1p1f1_gn_197001-200912\\huabeihur.nc')

# import xarray as xr

# # 打开NC文件
# dataset = xr.open_dataset('F:\\baiduunet\\0914\\CN05.1_Tm_1961_2021_daily_025x025\\CN05.1_Tm_1961_2021_daily_025x025.nc')
# print(dataset)
# # 获取经度和纬度的维度信息
# lon_dimension = dataset['lon'].values
# lat_dimension = dataset['lat'].values

# # 获取格点数
# lon_points = len(lon_dimension)
# lat_points = len(lat_dimension)

# print(f"经度格点数: {lon_points}")
# print(f"纬度格点数: {lat_points}")

# # 关闭文件（可选）
# # dataset.close()

import xarray as xr

# 打开NC文件
cn05_data = xr.open_dataset('F:\\baiduunet\\0914\\CN05.1_Tm_1961_2021_daily_025x025\\monthly.nc')
hur_data = xr.open_dataset('F:\\baiduunet\\0914\\CN05.1_Tm_1961_2021_daily_025x025\\huabeicmip6.nc')
tm_2010 = cn05_data['tm'].sel(time=slice('2010-01-01', '2010-12-31'))
hur_2010 = hur_data['hur'].sel(time=slice('2010-01-01', '2010-12-31'))

delta_hur = hur_2010 - tm_2010
downscale_hur = tm_2010 + delta_hur
downscale_hur.to_netcdf('F:\\baiduunet\\0914\\downscale_hur.nc')