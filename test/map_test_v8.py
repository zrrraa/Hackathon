import folium
from folium.plugins import MarkerCluster
import math

# 湖泊位置和基本信息数据
lake_data = {
    "佩枯措": {
        "lake_name": "佩枯措",
        "location": (88.54, 29.64),
        "area": "3.3",
        "capacity": "10000",
        "climate": "高原季风气候",
        "province": "西藏",
        "state": "暂无数据",
        "K_value": "0",
        "money": "0",
        "more": "F:\Hackathon\data\lake_moreabout\peikucuo.html"
    },
}

# 创建地图
m = folium.Map(
    [35.0, 105.0],
    tiles=
    'https://webst02.is.autonavi.com/appmaptile?style=6&x={x}&y={y}&z={z}',
    attr='高德-卫星影像图',
    zoom_start=5,
)

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
            /* 添加展开/折叠按钮样式 */
            .toggle-button {{
                background-color: #f1f1f1;
                color: #333;
                cursor: pointer;
                padding: 5px;
                border: none;
                width: 100%;
                text-align: left;
                outline: none;
                font-weight: bold;
            }}
            .toggle-content {{
                display: none;
                padding: 5px;
            }}
            .toggle-content.open {{
                display: block;
            }}
        </style>
        <script>
            // JavaScript function to toggle the content
            function toggleContent() {{
                var content = document.getElementById("input-content");
                content.classList.toggle("open");
            }}
        </script>
    </head>
    <body>
        <h1>{lake_name}</h1>
        <p>经度：{lon}度</p>
        <p>纬度：{lat}度</p>
        <p>面积：{area}平方公里</p>
        <p>容量：{capacity}</p>
        <p>气候：{climate}</p>
        
        <button class="toggle-button" onclick="toggleContent()">更新数据</button>
        <div id="input-content" class="toggle-content">
            <form id="input-form">
                <label for="year1">数据测量时间（第一年）：</label>
                <input type="text" id="year1" name="year1" required><br><br>
                <label for="biomass1">第一年生物量：</label>
                <input type="text" id="biomass1" name="biomass1" required><br><br>
                <label for="biomass2">第二年生物量：</label>
                <input type="text" id="biomass2" name="biomass2" required><br><br>
                <input type="button" value="计算" onclick="calculateValue()">
            </form>
        </div>
        
        <div id="output-value"></div>

        <div id="input-content" class="toggle-content">
            <form id="input-form">
                <label for="year1">数据测量时间（第一年）：</label>
                <input type="text" id="year1" name="year1" required><br><br>
                <label for="biomass1">第一年生物量：</label>
                <input type="text" id="biomass1" name="biomass1" required><br><br>
                <label for="biomass2">第二年生物量：</label>
                <input type="text" id="biomass2" name="biomass2" required><br><br>
                <input type="button" value="计算" onclick="calculateValue()">
            </form>
        </div>
        <script>
            var stateMessage = "";
            var value = 0;
            // JavaScript function to calculate the value
            function calculate_fishstate(year, biomass1, biomass2) {{
                // 计算
                var growth = biomass2 - biomass1;
                var intrinsic_growth_rate = 0.53;
                var biomass_v = biomass1;
                var K = intrinsic_growth_rate * Math.pow(biomass_v, 2) / (intrinsic_growth_rate * biomass_v - growth);
                var biomass0 = biomass1;

                if (biomass2 >= K / 2) {{
                    return 0; // 若可捕捞返回0
                }}

                var result = transcendental_equation(K, biomass0, intrinsic_growth_rate);
                if (result !== null) {{
                    return year + result - 2023; // 若不可捕捞返回预计几年后可以捕捞
                }}
                else return null;
            }}

            function transcendental_equation(K, biomass0, intrinsic_growth_rate) {{
                // 定义函数表达式
                function equation(t) {{
                    return K / (Math.exp(Math.log(K / biomass0 - 1) - intrinsic_growth_rate * t) + 1) - K / 2;
                }}

                // 定义函数的导数
                function derivative(t) {{
                    return K * intrinsic_growth_rate * Math.exp(Math.log(K / biomass0 - 1) - intrinsic_growth_rate * t) / ((Math.exp(Math.log(K / biomass0 - 1) - intrinsic_growth_rate * t) + 1) ** 2);
                }}

                // 初始化变量
                var t = 1.0; // 初始猜测值
                var epsilon = 1e-6; // 精度要求
                var max_iterations = 1000; // 最大迭代次数

                // 牛顿迭代法
                for (var i = 0; i < max_iterations; i++) {{
                    var f = equation(t);
                    var f_prime = derivative(t);
                    var delta_t = f / f_prime;
                    t -= delta_t;
                    if (Math.abs(delta_t) < epsilon) {{
                        return t; // 返回多少年后生物量达到K/2
                    }}
                }}

                // 如果超过最大迭代次数仍未找到解，则返回null
                return null;
            }}

            function adjust_fishstate(year, biomass) {{
                var K = 13696000; // 此处需要从信息卡中提取K值
                var intrinsic_growth_rate = 0.53;

                if (biomass >= K / 2) {{
                    return [0, 0]; // 若可捕捞则返回[0,0]
                }}

                var result = transcendental_equation(K, biomass, intrinsic_growth_rate);
                if (result >= 1) {{
                    return [1, year + result - 2023]; // 若禁渔则返回[1,禁渔时间]
                }} else {{
                    return [2, K / 2 - biomass]; // 若减少捕捞则返回[2,经济收益]
                    // 此处经济收益是（K/2-biomass）*money ！！！！
                }}
            }}

            // JavaScript function to toggle the content
            function toggleContent() {{
                var content = document.getElementById("input-content");
                content.classList.toggle("open");
            }}

            // JavaScript function to calculate the value
            function calculateValue() {{
                var year1 = parseFloat(document.getElementById("year1").value);
                var biomass1 = parseFloat(document.getElementById("biomass1").value);
                var biomass2 = parseFloat(document.getElementById("biomass2").value);
                value = calculate_fishstate(year1, biomass1, biomass2);
                var outputElement = document.getElementById("output-value");
                if (value === 0) {{
                    outputElement.innerHTML = "当前状态：可捕捞";
                }} else if (value !== null) {{
                    outputElement.innerHTML = "当前状态：" + String(value) + "年后可捕捞";
                }} else {{
                    outputElement.innerHTML = "当前状态：禁渔中";
                }}
            }}
        </script>
    </body>
    </html>
    """

    # 如果湖泊信息中有more信息，添加链接到另一个HTML页面
    if "more" in info:
        more_info_src = info["more"]
        html_content += f'<br><a href="{more_info_src}" target="_blank">更多信息</a>'

    iframe = folium.IFrame(html=html_content, width=480, height=320)
    popup = folium.Popup(iframe, max_width=2650)

    marker = folium.Marker([lat, lon], popup=popup)
    marker_cluster.add_child(marker)
    folium.Tooltip(lake_name).add_to(marker)

# 将标记聚类添加到地图
m.add_child(marker_cluster)

# 显示地图
m.save("output/china_lake_map.html")


def caculate_fishstate(year, biomass1,
                       biomass2):  #year是年 biomass1第一年生物量 biomass2第二年生物量 用于图0
    # 计算
    growth = biomass2 - biomass1
    intrinsic_growth_rate = 0.53
    biomass_v = biomass1
    K = intrinsic_growth_rate * pow(
        biomass_v, 2) / (intrinsic_growth_rate * biomass_v - growth)
    biomass0 = biomass1

    if biomass2 >= K / 2:
        return 0  #若可捕捞返回0

    result = transcendental_equation(K, biomass0, intrinsic_growth_rate)
    if result is not None:
        return (year + result - 2023)  #若不可捕捞返回预计几年后可以捕捞


def transcendental_equation(K, biomass0,
                            intrinsic_growth_rate):  #解超越方程，返回多少年后生物量达到K/2
    # 定义函数表达式
    def equation(t):
        return K / (
            math.exp(math.log(K / biomass0 - 1) - intrinsic_growth_rate * t) +
            1) - K / 2
# 定义函数的导数

    def derivative(t):
        return K * intrinsic_growth_rate * math.exp(
            math.log(K / biomass0 - 1) - intrinsic_growth_rate * t
        ) / (
            (math.exp(math.log(K / biomass0 - 1) - intrinsic_growth_rate * t) +
             1)**2)
# 初始化变量

    t = 1.0  # 初始猜测值
    epsilon = 1e-6  # 精度要求
    max_iterations = 1000  #最大迭代次数
    # 牛顿迭代法
    for i in range(max_iterations):
        f = equation(t)
        f_prime = derivative(t)
        delta_t = f / f_prime
        t -= delta_t
        if abs(delta_t) < epsilon:
            return t  #返回多少年后生物量达到K/2


# 如果超过最大迭代次数仍未找到解，则返回None
    return None