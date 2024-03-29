# -*- encoding: utf-8 -*-
"""
@File    :   nc2tif.py
@Time    :   2024/02/14 16:52:44
@Author  :   HMX
@Version :   1.0
@Contact :   kdhb8023@163.com
"""

# here put the import lib
from osgeo import gdal, osr
import xarray as xr
import numpy as np
import os


def main(fn, outfn):
    """tif2nc

    :param fn: 待处理nc文件路径
    :param outfn: 处理后tif文件路径
    """
    # 读取数据
    ds = xr.open_dataset(fn)
    # 根据时间求均值
    dsmean = ds.mean(dim='time')
    print(dsmean)

    # 读取变量
    data = dsmean['tas'].values
    print(data)
    print(data.shape)

    # 读取经纬度
    lon, lat = dsmean.lon.values, dsmean.lat.values
    # 计算分辨率
    res = lon[1] - lon[0]

    # 创建栅格
    driver = gdal.GetDriverByName("GTiff")
    output_dataset = driver.Create(outfn, len(lon), len(lat), 1, gdal.GDT_Float32)
    output_dataset.SetGeoTransform((lon.min(), res, 0, lat.max(), 0, -res))
    # 设置坐标系
    srs = osr.SpatialReference()
    srs.ImportFromEPSG(4326)
    output_dataset.SetProjection(srs.ExportToWkt())
    # 写入数据
    band = output_dataset.GetRasterBand(1)
    # 设置无效值
    band.SetNoDataValue(np.nan)
    band.WriteArray(np.flipud(data))
    output_dataset = None
    # print('ok')


if __name__ == '__main__':
    # 待处理nc文件路径
    fn = r'E:\MX\FM240214nc2tif\data\tas_126_I_2021_2040.nc'
    # 输出tif文件路径
    outfn = r'E:\MX\FM240214nc2tif\outdata\tas_126_I_2021_2040.tif'
    main(fn, outfn)
    print('ok')
