import arcpy
from arcpy import env
from arcpy.sa import *

# 设置工作空间
env.workspace = "D:/毕业论文.gdb"
# 添加raster
raster = "D:/毕业论文.gdb/投影49N2000"
arcpy.AddMessage("开始提取")
# 按属性提取
attExtract1 = ExtractByAttributes(raster, "地类 = '农田'")
arcpy.AddMessage("农田提取完成")
attExtract1.save("D:/毕业论文.gdb/农田2000")

attExtract2 = ExtractByAttributes(raster, "地类 = '森林'")
arcpy.AddMessage("森林提取完成")
attExtract2.save("D:/毕业论文.gdb/森林2000")

attExtract3 = ExtractByAttributes(raster, "地类 = '灌木'")
arcpy.AddMessage("灌木提取完成")
attExtract3.save("D:/毕业论文.gdb/灌木2000")

attExtract4 = ExtractByAttributes(raster, "地类 = '草地'")
arcpy.AddMessage("草地提取完成")
attExtract4.save("D:/毕业论文.gdb/草地2000")

attExtract5 = ExtractByAttributes(raster, "地类 = '水体'")
arcpy.AddMessage("水体提取完成")
attExtract5.save("D:/毕业论文.gdb/水体2000")

attExtract6 = ExtractByAttributes(raster, "地类 = '冰雪'")
arcpy.AddMessage("冰雪提取完成")
attExtract6.save("D:/毕业论文.gdb/冰雪2000")

attExtract7 = ExtractByAttributes(raster, "地类 = '荒地'")
arcpy.AddMessage("荒地提取完成")
attExtract7.save("D:/毕业论文.gdb/荒地2000")

attExtract8 = ExtractByAttributes(raster, "地类 = '不透水'")
arcpy.AddMessage("不透水提取完成")
attExtract8.save("D:/毕业论文.gdb/不透水2000")

attExtract9 = ExtractByAttributes(raster, "地类 = '湿地'")
arcpy.AddMessage("湿地提取完成")
attExtract9.save("D:/毕业论文.gdb/湿地2000")

