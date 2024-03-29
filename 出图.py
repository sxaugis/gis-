from osgeo import gdal
import matplotlib.pyplot as plt
# 打开gdb数据库中的栅格数据
dataset = gdal.Open("")
# 出图采用唯一值渲染
# 读取栅格数据的第一个波段
band = dataset.GetRasterBand(1)
# 读取栅格数据的第一个波段的数据
data = band.ReadAsArray()
# 出图采用唯一值渲染色带从蓝到红
plt.imshow(data, cmap=plt.cm.Blues_r)
plt.show()