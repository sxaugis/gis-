import xarray as xr
import numpy as np


ds = xr.open_dataset('F:/baiduunet/0117nc/sel_china_remapcon_tas_day_BCC_historical_1975-2014_3_5_cn05grid_downscaled_nothern_sel.nc')
weights = np.cos(np.deg2rad(ds.lat))
ds_weighted = ds.weighted(weights)
ds_weighted_mean = ds_weighted.mean(('lat', 'lon'))
temp = ds_weighted_mean['tas']
temp_year = temp.groupby('time.year').mean('time')
df = temp_year.to_dataframe()
df.to_csv('F:/baiduunet/0117nc/1975-2014年平均温度.csv',encoding='utf-8-sig')