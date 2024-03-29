import xarray as xr
import numpy as np

ds = xr.open_dataset('F:/baiduunet/0117nc/sel_china_remapcon_tas_day_BCC_historical_1975-2014_3_5_cn05grid_downscaled_nothern_sel.nc')
weights = np.cos(np.deg2rad(ds.lat))
ds_weighted = ds.weighted(weights)
ds_weighted_mean = ds_weighted.mean(('lat', 'lon'))
temp = ds_weighted_mean['tas']
temp_change = temp.diff('time')
rolling_temp_change = temp_change.rolling(time=7).mean()
max_temp_diff = rolling_temp_change.groupby('time.year').min('time')
min_mean_change = max_temp_diff.min()
df = min_mean_change.to_dataframe()
df.to_csv('F:/baiduunet/0117nc/1975-2014最大降温幅度',encoding='utf-8-sig')