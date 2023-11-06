import folium
from folium.plugins import MarkerCluster


# 湖泊位置和基本信息数据
lake_data = {
    "佩枯措": {
        "lake_name": "佩枯措",
        "location": (88.54, 29.64),
        "area": "3.3",
        "capacity": "0",
        "climate": "高原季风气候",
        "province": "西藏",
        "state": "暂无数据",
        "K_value": "0",
        "money": "0",
        "more": "F:\Hackathon\data\lake_moreabout\peikucuo.html"
    },
}

# 创建地图

m = folium.Map([35.0, 105.0],
  tiles= 'https://webst02.is.autonavi.com/appmaptile?style=6&x={x}&y={y}&z={z}',
  attr='高德-卫星影像图',
  zoom_start=5,
  )

# m = folium.Map([35.0, 105.0],
#     tiles='http://thematic.geoq.cn/arcgis/rest/services/ThematicMaps/WorldHydroMap/MapServer/tile/{z}/{y}/{x}',
#     attr='水系专题',
#     zoom_start=5,
#     )

# 创建标记聚类
marker_cluster = MarkerCluster()

# 添加湖泊标记及面积和气候信息
for lake_name, info in lake_data.items():
    lon, lat = info["location"]
    area = info["area"]
    capacity = info["capacity"]
    climate = info["climate"]
    state = info["state"]

    # 创建自定义HTML内容
    html_content = f"""
    <html>
    <head>
        <title>{lake_name}</title>
        <style>
            /* 添加按钮样式 */
            body {{
                font-family: "Microsoft YaHei", Arial, sans-serif;
                color: black; /* 设置字体颜色为黑色 */
            }}

            #calculateButton {{
                margin-top: 20px; /* 增加与上面内容的垂直间距 */
                padding: 10px 30px; /* 增大按钮的尺寸 */
            }}
        </style>
    </head>
    <body>
        <h1>{lake_name}</h1>
        <p>经度：{lon}度</p>
        <p>纬度：{lat}度</p>
        <p>面积：{area}平方公里</p>
        <p>容量：{capacity}</p>
        <p>气候：{climate}</p>

        <h2>计算环境容纳量</h2>
        <table style="margin: 0 auto;">
            <tr>
                <th></th>
                <th>大鱼生物量</th>
                <th>小鱼生物量</th>
            </tr>
            <tr>
                <th>第一年</th>
                <td><input type="text" id="row2col2" style="height: 30px;"></td>
                <td><input type="text" id="row2col3" style="height: 30px;"></td>
            </tr>
            <tr>
                <th>第二年</th>
                <td><input type="text" id="row3col2" style="height: 30px;"></td>
                <td><input type="text" id="row3col3" style="height: 30px;"></td>
            </tr>
        </table>

        <!-- 计算按钮 -->
        <button id="calculateButton">计算</button>

        <!-- 增加间距 -->
        <br>

        <!-- 标签框用于显示总和 -->
        <p id="sum" style="display: none;">等待计算结果...</p>
    """

    # 如果湖泊信息中有more信息，添加链接到另一个HTML页面
    if "more" in info:
        more_info_src = info["more"]
        html_content += f'<br><a href="{more_info_src}" target="_blank">更多信息</a>'

    html_content += """

        <script>
            const inputElements = document.querySelectorAll("input:not([type='text'][id='row2col1'], [type='text'][id='row3col1'], [type='text'][id='row1col2'], [type='text'][id='row1col3'])");
            const sumElement = document.getElementById("sum");
            const calculateButton = document.getElementById("calculateButton");

            calculateButton.addEventListener("click", calculateSum);

            function calculateSum() {
                let total = 0;
                inputElements.forEach((inputElement) => {
                    const inputValue = parseFloat(inputElement.value) || 0;
                    total += inputValue;
                });
                sumElement.textContent = "环境容纳量：" + total;
                sumElement.style.display = "block";
            }
        </script>
        
    </body>
    </html>
    """

    iframe = folium.IFrame(html=html_content, width=480, height=320)
    popup = folium.Popup(iframe, max_width=2650)

    marker = folium.Marker([lat, lon], popup=popup)
    marker_cluster.add_child(marker)
    folium.Tooltip(lake_name).add_to(marker)

# 将标记聚类添加到地图
m.add_child(marker_cluster)

# 显示地图
m.save("output/china_lake_map.html")
