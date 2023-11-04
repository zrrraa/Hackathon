import folium
from folium import IFrame

# 创建地图
m = folium.Map(location=[35.0, 105.0], zoom_start=5)

# 创建标记
marker = folium.Marker(
    location=[35, 105],
    popup=folium.Popup(
        '<img src="peikucuo_map.jpg" alt="Image" width="200" height="200">',
        max_width=250))

# 将标记添加到地图上
marker.add_to(m)

# 显示地图
m.save('test/map.html')