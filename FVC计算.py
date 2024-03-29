from  osgeo  import  gdal
import numpy as np
import os
import glob

# 设置输入和输出文件夹路径
input_folder = 'E:/gis/毕业论文/康/kang-20230425T083036Z-001/kang'
output_folder = 'E:/gis/毕业论文/康/fvc'

# 设置 FVC 计算参数
l_bound = 0.05
u_bound = 0.95
n_iter = 100

# 批量处理 TIFF 文件
tif_files = glob.glob(os.path.join(input_folder, '*.tif'))
for tif_file in tif_files:
    # 读取 NDVI 数据
    ndvi_dataset = gdal.Open(tif_file)
    ndvi_band = ndvi_dataset.GetRasterBand(1)
    ndvi_array = np.array(ndvi_band.ReadAsArray())

    # 将 NDVI 的值为 0 的像元赋为 -0.1
    ndvi_array[ndvi_array == 0] = -0.1

    # 计算 FVC
    fvc_array = np.zeros_like(ndvi_array, dtype=np.float32)
    for i in range(ndvi_array.shape[0]):
        for j in range(ndvi_array.shape[1]):
            ndvi = ndvi_array[i, j]
            if ndvi <= l_bound:
                fvc = 0
            elif ndvi >= u_bound:
                fvc = 1
            else:
                fvc_lower = 0
                fvc_upper = 1
                for k in range(n_iter):
                    fvc_mid = (fvc_lower + fvc_upper) / 2
                    ndvi_mid = (fvc_mid - 1) * ndvi / (fvc_mid - ndvi)
                    if ndvi_mid > l_bound:
                        fvc_lower = fvc_mid
                    else:
                        fvc_upper = fvc_mid
                fvc = fvc_mid
            fvc_array[i, j] = fvc

    # 将结果保存为 GeoTIFF 文件
    basename = os.path.basename(tif_file)
    output_file = os.path.join(output_folder, f'fvc_{basename}')
    driver = gdal.GetDriverByName('GTiff')
    fvc_dataset = driver.Create(output_file,
                                ndvi_array.shape[1], ndvi_array.shape[0], 1, gdal.GDT_Float32)
    fvc_dataset.SetProjection(ndvi_dataset.GetProjection())
    fvc_dataset.SetGeoTransform(ndvi_dataset.GetGeoTransform())
    fvc_band = fvc_dataset.GetRasterBand(1)
    fvc_band.WriteArray(fvc_array)
    fvc_band.FlushCache()
    fvc_band.SetNoDataValue(-9999)
    fvc_band.ComputeStatistics(False)
    fvc_dataset.FlushCache()

