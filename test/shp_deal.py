import geopandas as gpd
import matplotlib.pyplot as plt

data = r"F:\Hackathon\data\lake_shapefiles\Qinghai_Lake\Qinghai_Lake.shp"

# 使用geopandas读取.shp文件
gdf = gpd.read_file(data)

# 打印数据的前几行
print(gdf.head())

# 可以进一步处理和分析地理空间数据
# 例如，绘制地图
gdf.plot()

# 保存地图为 JPEG 图像
plt.savefig("data\lake_images\qinghaihu\qinghaihu.jpg")

# 显示地图
plt.show()
