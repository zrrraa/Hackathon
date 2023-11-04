import folium
import geopandas as gpd
import matplotlib.pyplot as plt

# 湖泊位置和基本信息数据
lake_data = {
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
    },
    "佩枯措": {
        "location": (88.54, 29.64),
        "area": "3.3 km\u00B2"
    }
    # 添加更多湖泊位置和信息
}

# 创建地图
m = folium.Map(location=[35.0, 105.0], zoom_start=5)

# 添加湖泊标记及面积信息
for lake_name, info in lake_data.items():
    lon, lat = info["location"]
    area = info["area"]
    
    # 创建自定义HTML内容
    html_content = f"""
    <html>
    <head>
        <title>{lake_name}</title>
    </head>
    <body>
        <h1>{lake_name}</h1>
        <p>面积: {area} 平方公里</p>
        <p>这里可以放更多内容</p>
    </body>
    </html>
    """
    
    iframe = folium.IFrame(html=html_content, width=400, height=300)
    popup = folium.Popup(iframe, max_width=2650)
    
    marker = folium.Marker([lat, lon], popup=popup)
    marker.add_to(m)
    folium.Tooltip(lake_name).add_to(marker)

# 显示地图
m.save("china_lake_map.html")
