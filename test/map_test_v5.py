import folium
from folium.plugins import MarkerCluster

# 湖泊位置和基本信息数据
lake_data = {
    "巢湖": {
        "lake_name": "巢湖",
        "location": (117.38, 31.62),
        "area": "2,800",
        "climate": "温带季风气候"
    },
    "洞庭湖": {
        "lake_name": "洞庭湖",
        "location": (112.95, 29.46),
        "area": "2,680",
        "climate": "温带季风气候"
    },
    "鄱阳湖": {
        "lake_name": "鄱阳湖",
        "location": (116.00, 29.71),
        "area": "3,500",
        "climate": "亚热带季风气候"
    },
    "太湖": {
        "lake_name": "太湖",
        "location": (120.13, 31.16),
        "area": "2,250",
        "climate": "亚热带季风气候"
    },
    "西湖": {
        "lake_name": "西湖",
        "location": (120.14, 30.24),
        "area": "6.39",
        "climate": "亚热带季风气候"
    },
    "滇池": {
        "lake_name": "滇池",
        "location": (102.68, 24.48),
        "area": "71.67",
        "climate": "亚热带季风气候"
    },
    "青海湖": {
        "lake_name": "青海湖",
        "location": (99.94, 36.73),
        "area": "4,317",
        "climate": "高原季风气候"
    },
    "洪泽湖": {
        "lake_name": "洪泽湖",
        "location": (118.80, 33.46),
        "area": "1,368",
        "climate": "温带季风气候"
    },
    "麦积湖": {
        "lake_name": "麦积湖",
        "location": (105.95, 34.57),
        "area": "23.5",
        "climate": "温带季风气候"
    },
    "洪湖": {
        "lake_name": "洪湖",
        "location": (113.46, 29.81),
        "area": "2,450",
        "climate": "亚热带季风气候"
    },
    "黑龙潭": {
        "lake_name": "黑龙潭",
        "location": (126.66, 45.69),
        "area": "0.42",
        "climate": "寒温带季风气候"
    },
    "乌鲁木齐市湖": {
        "lake_name": "乌鲁木齐市湖",
        "location": (87.62, 43.79),
        "area": "0.06",
        "climate": "温带干旱气候"
    },
    "青龙潭": {
        "lake_name": "青龙潭",
        "location": (121.41, 24.97),
        "area": "0.41",
        "climate": "亚热带季风气候"
    },
    "佩枯措": {
        "lake_name": "佩枯措",
        "location": (88.54, 29.64),
        "area": "3.3",
        "climate": "高原季风气候"
    },
    "青海湖": {
        "lake_name": "青海湖",
        "location": (99.94, 36.73),
        "area": "4,317",
        "climate": "高原季风气候"
    },
    "千岛湖": {
        "lake_name": "千岛湖",
        "location": (118.93, 29.56),
        "area": "573",
        "climate": "亚热带季风气候"
    },
    "瓯江口海域": {
        "lake_name": "瓯江口海域",
        "location": (120.62, 27.99),
        "area": "1,500",
        "climate": "亚热带季风气候"
    },
    "黄河干流岩锅峡——黑山峡段": {
        "lake_name": "黄河干流岩锅峡——黑山峡段",
        "location": (110.78, 36.61),
        "area": "28",
        "climate": "温带季风气候"
    },
    "厦门海域": {
        "lake_name": "厦门海域",
        "location": (118.10, 24.52),
        "area": "200",
        "climate": "亚热带季风气候"
    },
    "乐清湾": {
        "lake_name": "乐清湾",
        "location": (120.91, 28.08),
        "area": "75",
        "climate": "亚热带季风气候"
    },
    "天津近岸海域": {
        "lake_name": "天津近岸海域",
        "location": (117.66, 38.83),
        "area": "300",
        "climate": "温带季风气候"
    },
    "闽江口及附近海域": {
        "lake_name": "闽江口及附近海域",
        "location": (119.72, 25.85),
        "area": "400",
        "climate": "亚热带季风气候"
    },
    "南朗水域": {
        "lake_name": "南朗水域",
        "location": (113.52, 22.45),
        "area": "2",
        "climate": "亚热带季风气候"
    }
}

# 创建地图
m = folium.Map(location=[35.0, 105.0], zoom_start=5)

# 创建标记聚类
marker_cluster = MarkerCluster()

# 添加湖泊标记及面积和气候信息
for lake_name, info in lake_data.items():
    lon, lat = info["location"]
    area = info["area"]
    climate = info["climate"]

    # 创建自定义HTML内容
    html_content = f"""
    <html>
    <head>
        <title>{lake_name}</title>
    </head>
    <body>
        <h1>{lake_name}</h1>
        <p>经度：{lon}度</p>
        <p>纬度：{lat}度</p>
        <p>面积：{area}平方公里</p>
        <p>气候：{climate}</p>
        <p>这里可以放更多内容</p>
    </body>
    </html>
    """

    iframe = folium.IFrame(html=html_content, width=480, height=300)
    popup = folium.Popup(iframe, max_width=2650)

    marker = folium.Marker([lat, lon], popup=popup)
    marker_cluster.add_child(marker)
    folium.Tooltip(lake_name).add_to(marker)

# 将标记聚类添加到地图
m.add_child(marker_cluster)

# 显示地图
m.save("output/china_lake_map.html")
