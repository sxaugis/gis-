import arcpy
from arcpy import env
env.workspace = "F:/数据/掩膜数据"
outWorkspace = "F:/数据/平均值"
rasters = arcpy.ListRasters("*", "TIF")
cellStats = arcpy.sa.CellStatistics(rasters, "MEAN")
cellStats.save(outWorkspace + "/mean.tif")