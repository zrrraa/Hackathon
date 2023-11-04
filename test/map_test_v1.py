import matplotlib.pyplot as plt
import cartopy
import cartopy.crs as ccrs
import mplcursors

import matplotlib as mpl

# 设置中文字体
mpl.rcParams['font.family'] = 'Microsoft YaHei'

# 湖泊位置和基本信息数据
lake_positions = {
    "巢湖": {
        "location": (117.38, 31.62),
        "area": "2,800 km\u00B2"
    },
    "洞庭湖": {
        "location": (112.95, 29.46),
        "area": "2,680 km\u00B2"
    },
    "鄱阳湖": {
        "location": (116.00, 29.71),
        "area": "3,500 km\u00B2"
    },
    "太湖": {
        "location": (120.13, 31.16),
        "area": "2,250 km\u00B2"
    },
    "西湖": {
        "location": (120.14, 30.24),
        "area": "6.39 km\u00B2"
    },
    "滇池": {
        "location": (102.68, 24.48),
        "area": "71.67 km\u00B2"
    },
    "青海湖": {
        "location": (99.94, 36.73),
        "area": "4,317 km\u00B2"
    },
    "洪泽湖": {
        "location": (118.80, 33.46),
        "area": "1,368 km\u00B2"
    },
    "麦积湖": {
        "location": (105.95, 34.57),
        "area": "23.5 km\u00B2"
    },
    "洪湖": {
        "location": (113.46, 29.81),
        "area": "2,450 km\u00B2"
    },
    "黑龙潭": {
        "location": (126.66, 45.69),
        "area": "0.42 km\u00B2"
    },
    "乌鲁木齐市湖": {
        "location": (87.62, 43.79),
        "area": "0.06 km\u00B2"
    },
    "青龙潭": {
        "location": (121.41, 24.97),
        "area": "0.41 km\u00B2"
    }
    # 添加更多湖泊位置和信息
}

# 绘制中国地图
def plot_china_map():
    # 创建地图投影
    ax = plt.axes(projection=ccrs.PlateCarree())

    # 绘制海岸线、国家边界线等
    ax.coastlines()
    ax.add_feature(cartopy.feature.BORDERS, linestyle='-', alpha=0.5)

    # 绘制湖泊位置
    for lake_name, info in lake_positions.items():
        lon, lat = info["location"]
        ax.plot(lon, lat, 'ro', markersize=5, transform=ccrs.PlateCarree())

    # 设置地图范围
    ax.set_extent([73.5, 135.0, 18.0, 53.5])

    # 添加鼠标悬停提示
    mplcursors.cursor(hover=True).connect(
        "add", lambda sel: sel.annotation.set_text(
            get_lake_info(sel.target[0], sel.target[1])))

    # 添加双击事件处理函数
    def on_double_click(event):
        if event.dblclick:
            lon, lat = event.xdata, event.ydata
            lake_info = get_lake_info(lon, lat)
            if lake_info:
                # 根据湖泊位置放大地图区域
                ax.set_extent([lon - 1, lon + 1, lat - 1, lat + 1])
                plt.title(f"Zoomed In: {lake_info}")
                plt.draw()

    # 连接双击事件处理函数
    plt.connect('button_press_event', on_double_click)

    # 显示图例、标题等
    plt.title("China Map with Major Lakes")
    plt.legend(["Lakes"])

    # 显示地图
    plt.show()


# 获取湖泊信息
def get_lake_info(lon, lat):
    for lake_name, info in lake_positions.items():
        if info["location"] == (lon, lat):
            return f"Lake: {lake_name}\nArea: {info['area']}"
    return ""


# 调用函数绘制地图
plot_china_map()