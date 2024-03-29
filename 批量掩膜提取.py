import arcpy
import os
import arcpy.sa
import time

# 设置工作空间
arcpy.env.workspace = "F:/数据/SCD"
print(arcpy.env.workspace)
# 获取文件夹下的所有tiff文件
rasterList = arcpy.ListRasters("*", "TIF")
# 导入掩膜
shp = "F:/数据/ssss/beiffffff.shp"
print(rasterList)
# 批量掩膜提取并保存为新的tiff文件
for raster in rasterList:
    # 记录开始时间
    start = time.time()
    print(raster + "开始提取")
    outExtractByMask = arcpy.sa.ExtractByMask(raster, shp)
    # 获取文件名
    rasterName = os.path.splitext(raster)[0]
    # 保存提取后的文件
    outExtractByMask.save(os.path.join("F:/数据/掩膜数据/", rasterName +"掩膜.tif"))
    #记录结束时间
    end = time.time()
    print("提取时间为：", end - start)