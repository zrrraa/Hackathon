import geopandas as gpd
import matplotlib.pyplot as plt

data = r"1975-2021年佩枯措矢量和面积数据\1975-2021年佩枯措矢量和面积数据\佩枯措1975-2021年矢量数据\2021年\20211010佩枯错.shp"

# 使用geopandas读取.shp文件
gdf = gpd.read_file(data)

# 打印数据的前几行
print(gdf.head())

# 可以进一步处理和分析地理空间数据
# 例如，绘制地图
gdf.plot()

# 保存地图为 JPEG 图像
plt.savefig("data\lake_images\peikucuo_map.png")

# 显示地图
plt.show()
