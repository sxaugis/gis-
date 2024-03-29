import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
nc_file = 'F:/baiduunet/0117nc/cn05grid_remap_regrid_china_hur_day_BCC_historical_1985-1994_3_5_downscaled_nothern_sel.nc'
ds = xr.open_dataset(nc_file)
weights = np.cos(np.deg2rad(ds.lat))
ds_weighted = ds.weighted(weights)
ds_weighted_mean = ds_weighted.mean(('lat', 'lon'))
ds_weighted_mean =  ds_weighted_mean.sel(plev=10000)
ds_weighted_mean_year = ds_weighted_mean.groupby('time.year').mean('time')
print(ds_weighted_mean_year)
ds_weighted_mean_year_10000 = ds_weighted_mean_year.sel(plev=10000)
df = ds_weighted_mean_year_10000.to_dataframe()
df = df.drop(['plev'],axis=1)
df.to_csv('F:/baiduunet/0117nc/1985-1994年平均气压.csv',encoding='utf-8-sig')