import folium
from folium.plugins import MarkerCluster
import math

# 湖泊位置和基本信息数据
lake_data = {
    "巢湖": {
        "lake_name": "巢湖",
        "province": "安徽省",
        "location": (117.38, 31.62),
        "area": "2,800",
        "capacity": "0",
        "climate": "温带季风气候",
        "state": "暂无数据",
        "K_value": 0,
        "money": 0
    },
    "洞庭湖": {
        "lake_name": "洞庭湖",
        "province": "湖南省",
        "location": (112.95, 29.46),
        "area": "2,680",
        "capacity": "0",
        "climate": "温带季风气候",
        "state": "暂无数据",
        "K_value": 0,
        "money": 0
    },
    "鄱阳湖": {
        "lake_name": "鄱阳湖",
        "province": "江西省",
        "location": (116.00, 29.71),
        "area": "3,500",
        "capacity": "0",
        "climate": "亚热带季风气候",
        "state": "暂无数据",
        "K_value": 0,
        "money": 0
    },
    "太湖": {
        "lake_name": "太湖",
        "province": "江苏省",
        "location": (120.13, 31.16),
        "area": "2,250",
        "capacity": "0",
        "climate": "亚热带季风气候",
        "state": "暂无数据",
        "K_value": 0,
        "money": 0
    },
    "西湖": {
        "lake_name": "西湖",
        "province": "浙江省",
        "location": (120.14, 30.24),
        "area": "6.39",
        "capacity": "0",
        "climate": "亚热带季风气候",
        "state": "暂无数据",
        "K_value": 0,
        "money": 0
    },
    "滇池": {
        "lake_name": "滇池",
        "province": "云南省",
        "location": (102.68, 24.48),
        "area": "71.67",
        "capacity": "0",
        "climate": "亚热带季风气候",
        "state": "暂无数据",
        "K_value": 0,
        "money": 0
    },
    "青海湖": {
        "lake_name": "青海湖",
        "province": "青海省",
        "location": (99.94, 36.73),
        "area": "4,317",
        "capacity": "0",
        "climate": "高原季风气候",
        "state": "暂无数据",
        "K_value": 0,
        "money": 32.7377394,
        "more": "F:\Hackathon\data\lake_moreabout\qinghaihu.html"
    },
    "洪泽湖": {
        "lake_name": "洪泽湖",
        "province": "江苏省",
        "location": (118.80, 33.46),
        "area": "1,368",
        "capacity": "0",
        "climate": "温带季风气候",
        "state": "暂无数据",
        "K_value": 0,
        "money": 0
    },
    "麦积湖": {
        "lake_name": "麦积湖",
        "province": "甘肃省",
        "location": (105.95, 34.57),
        "area": "23.5",
        "capacity": "0",
        "climate": "温带季风气候",
        "state": "暂无数据",
        "K_value": 0,
        "money": 0
    },
    "洪湖": {
        "lake_name": "洪湖",
        "province": "湖北省",
        "location": (113.46, 29.81),
        "area": "2,450",
        "capacity": "0",
        "climate": "亚热带季风气候",
        "state": "暂无数据",
        "K_value": 0,
        "money": 0
    },
    "黑龙潭": {
        "lake_name": "黑龙潭",
        "province": "吉林省",
        "location": (126.66, 45.69),
        "area": "0.42",
        "capacity": "0",
        "climate": "寒温带季风气候",
        "state": "暂无数据",
        "K_value": 0,
        "money": 0
    },
    "青龙潭": {
        "lake_name": "青龙潭",
        "province": "台湾省",
        "location": (121.41, 24.97),
        "area": "0.41",
        "capacity": "0",
        "climate": "亚热带季风气候",
        "state": "暂无数据",
        "K_value": 0,
        "money": 0
    },
    "佩枯措": {
        "lake_name": "佩枯措",
        "province": "西藏自治区",
        "location": (88.54, 29.64),
        "area": "3.3",
        "capacity": "0",
        "climate": "高原季风气候",
        "state": "暂无数据",
        "K_value": 0,
        "money": 22,
        "more": "F:\Hackathon\data\lake_moreabout\peikucuo.html"
    },
    "千岛湖": {
        "lake_name": "千岛湖",
        "location": [118.93, 29.56],
        "area": "573",
        "climate": "亚热带季风气候",
        "province": "浙江省",
        "K_value": 0,
        "state": "暂无数据",
        "money": 0,
        "capacity": 0
    },
    "瓯江口海域": {
        "lake_name": "瓯江口海域",
        "location": [120.62, 27.99],
        "area": "1,500",
        "climate": "亚热带季风气候",
        "province": "福建省",
        "K_value": 0,
        "state": "暂无数据",
        "money": 0,
        "capacity": 0
    },
    "黄河干流岩锅峡——黑山峡段": {
        "lake_name": "黄河干流岩锅峡——黑山峡段",
        "location": [110.78, 36.61],
        "area": "28",
        "climate": "温带季风气候",
        "province": "河南省",
        "K_value": 0,
        "state": "暂无数据",
        "money": 0,
        "capacity": 0
    },
    "厦门海域": {
        "lake_name": "厦门海域",
        "location": [118.10, 24.52],
        "area": "200",
        "climate": "亚热带季风气候",
        "province": "福建省",
        "K_value": 0,
        "state": "暂无数据",
        "money": 0,
        "capacity": 0
    },
    "乐清湾": {
        "lake_name": "乐清湾",
        "location": [120.91, 28.08],
        "area": "75",
        "climate": "亚热带季风气候",
        "province": "浙江省",
        "K_value": 0,
        "state": "暂无数据",
        "money": 0,
        "capacity": 0
    },
    "天津近岸海域": {
        "lake_name": "天津近岸海域",
        "location": [117.66, 38.83],
        "area": "300",
        "climate": "温带季风气候",
        "province": "天津市",
        "K_value": 0,
        "state": "暂无数据",
        "money": 0,
        "capacity": 0
    },
    "闽江口及附近海域": {
        "lake_name": "闽江口及附近海域",
        "location": [119.72, 25.85],
        "area": "400",
        "climate": "亚热带季风气候",
        "province": "福建省",
        "K_value": 0,
        "state": "暂无数据",
        "money": 0,
        "capacity": 0
    },
    "南朗水域": {
        "lake_name": "南朗水域",
        "location": [113.52, 22.45],
        "area": "2",
        "climate": "亚热带季风气候",
        "province": "广东省",
        "K_value": 0,
        "state": "暂无数据",
        "money": 0,
        "capacity": 0
    },
    "呼伦湖": {
        "lake_name": "呼伦湖",
        "location": (119.66, 49.11),
        "area": "2,339",
        "climate": "寒温带季风气候",
        "province": "内蒙古",
        "K_value": 0,
        "state": "暂无数据",
        "money": 0,
        "capacity": 0
    },
    "长江天鹅洲故道": {
        "lake_name": "长江天鹅洲故道",
        "location": (118.33, 29.97),
        "area": "154",
        "climate": "亚热带季风气候",
        "province": "浙江",
        "K_value": 0,
        "state": "暂无数据",
        "money": 0,
        "capacity": 0
    },
    "贝尔湖": {
        "lake_name": "贝尔湖",
        "location": (126.77, 50.83),
        "area": "1,160",
        "climate": "寒温带季风气候",
        "province": "黑龙江",
        "K_value": 0,
        "state": "暂无数据",
        "money": 0,
        "capacity": 0
    },
    "大兴凯湖": {
        "lake_name": "大兴凯湖",
        "location": (123.73, 51.53),
        "area": "2,340",
        "climate": "寒温带季风气候",
        "province": "黑龙江",
        "K_value": 0,
        "state": "暂无数据",
        "money": 0,
        "capacity": 0
    },
    "小兴凯湖": {
        "lake_name": "小兴凯湖",
        "location": (123.60, 51.49),
        "area": "942",
        "climate": "寒温带季风气候",
        "province": "黑龙江",
        "K_value": 0,
        "state": "暂无数据",
        "money": 0,
        "capacity": 0
    },
    "连环湖": {
        "lake_name": "连环湖",
        "location": (113.13, 23.61),
        "area": "0.33",
        "climate": "亚热带季风气候",
        "province": "广东",
        "K_value": 0,
        "state": "暂无数据",
        "money": 0,
        "capacity": 0
    },
    "莲花湖": {
        "lake_name": "莲花湖",
        "location": (116.05, 29.75),
        "area": "0.34",
        "climate": "亚热带季风气候",
        "province": "湖南",
        "K_value": 0,
        "state": "暂无数据",
        "money": 0,
        "capacity": 0
    },
    "达里加湖": {
        "lake_name": "达里加湖",
        "location": (131.65, 45.37),
        "area": "1.15",
        "climate": "寒温带季风气候",
        "province": "黑龙江",
        "K_value": 0,
        "state": "暂无数据",
        "money": 0,
        "capacity": 0
    },
    "卧龙湖": {
        "lake_name": "卧龙湖",
        "location": (103.48, 29.99),
        "area": "0.1",
        "climate": "亚热带季风气候",
        "province": "四川",
        "K_value": 0,
        "state": "暂无数据",
        "money": 0,
        "capacity": 0
    },
    "长白山天池": {
        "lake_name": "长白山天池",
        "location": (127.92, 41.68),
        "area": "9.05",
        "climate": "寒温带季风气候",
        "province": "吉林",
        "K_value": 0,
        "state": "暂无数据",
        "money": 0,
        "capacity": 0
    },
    "查干湖": {
        "lake_name": "查干湖",
        "location": (104.52, 44.13),
        "area": "0.73",
        "climate": "寒温带季风气候",
        "province": "内蒙古",
        "K_value": 0,
        "state": "暂无数据",
        "money": 0,
        "capacity": 0
    },
    "雁鸣湖": {
        "lake_name": "雁鸣湖",
        "location": (115.79, 40.94),
        "area": "1.64",
        "climate": "温带季风气候",
        "province": "河北",
        "K_value": 0,
        "state": "暂无数据",
        "money": 0,
        "capacity": 0
    },
    "南丽湖": {
        "lake_name": "南丽湖",
        "location": (108.44, 21.92),
        "area": "0.12",
        "climate": "亚热带季风气候",
        "province": "广西",
        "K_value": 0,
        "state": "暂无数据",
        "money": 0,
        "capacity": 0
    },
    "喀斯那湖": {
        "lake_name": "喀斯那湖",
        "location": (80.09, 31.57),
        "area": "1.82",
        "climate": "温带季风气候",
        "province": "四川省",
        "K_value": 0,
        "state": "暂无数据",
        "money": 0,
        "capacity": 0
    },
    "清潩河武昌段": {
        "lake_name": "清潩河武昌段",
        "location": (114.27, 30.56),
        "area": "待提供",
        "climate": "亚热带季风气候",
        "province": "湖北省",
        "K_value": 0,
        "state": "暂无数据",
        "money": 0,
        "capacity": 0
    },
    "洈水水库": {
        "lake_name": "洈水水库",
        "location": (119.27, 31.47),
        "area": "待提供",
        "climate": "温带季风气候",
        "province": "浙江省",
        "K_value": 0,
        "state": "暂无数据",
        "money": 0,
        "capacity": 0
    },
    "白洋淀": {
        "lake_name": "白洋淀",
        "location": (115.40, 39.51),
        "area": "待提供",
        "climate": "温带季风气候",
        "province": "河北省",
        "K_value": 0,
        "state": "暂无数据",
        "money": 0,
        "capacity": 0
    },
    "珠江口": {
        "lake_name": "珠江口",
        "location": (113.27, 22.59),
        "area": "400",
        "climate": "热带季风气候",
        "province": "广东省",
        "K_value": 0,
        "state": "暂无数据",
        "money": 0,
        "capacity": 0
    },
    "胶州湾": {
        "lake_name": "胶州湾",
        "location": (120.00, 36.15),
        "area": "343.1",
        "climate": "温带季风气候",
        "province": "山东省",
        "K_value": 0,
        "state": "暂无数据",
        "money": 0,
        "capacity": 0
    },
    "滆湖": {
        "lake_name": "滆湖",
        "location": (115.45, 38.40),
        "area": "164",
        "climate": "温带大陆性季风气候",
        "province": "河北省",
        "K_value": 0,
        "state": "暂无数据",
        "money": 0,
        "capacity": 0
    },
    "五里湖": {
        "lake_name": "五里湖",
        "location": (116.30, 40.05),
        "area": "8.4",
        "climate": "温带季风气候",
        "province": "北京市",
        "K_value": 0,
        "state": "暂无数据",
        "money": 0,
        "capacity": 0
    }
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
    province = info["province"]
    money = info["money"]
    K_value = info["K_value"]

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
            function toggleContent1() {{
                var content = document.getElementById("input-content1");
                content.classList.toggle("open");
            }}
            function toggleContent2() {{
                var content = document.getElementById("input-content2");
                content.classList.toggle("open");
            }}
        </script>
    </head>
    <body>
        <h1>{lake_name}</h1>
        <p>经度：{lon}度</p>
        <p>纬度：{lat}度</p>
        <p>省份：{province}</p>
        <p>面积：{area}平方公里</p>
        <p>容量：{capacity}</p>
        <p>气候：{climate}</p>
        <p>经济效应参数：{money}</p>

        <button class="toggle-button" onclick="toggleContent1()">添加数据</button>
        <div id="input-content1" class="toggle-content">
            <form id="input-form">
                <label for="year1">数据测量时间（第一年）：</label>
                <input type="text" id="year1" name="year1" required><br><br>
                <label for="biomass1">第一年生物量：</label>
                <input type="text" id="biomass1" name="biomass1" required><br><br>
                <label for="biomass2">第二年生物量：</label>
                <input type="text" id="biomass2" name="biomass2" required><br><br>
                <input type="button" value="计算" onclick="calculateValue1()">
            </form>
        </div>

        <button class="toggle-button" onclick="toggleContent2()">更新数据</button>
        <div id="input-content2" class="toggle-content">
            <form id="input-form">
                <label for="year">数据测量时间：</label>
                <input type="text" id="year" name="year" required><br><br>
                <label for="biomass">鱼类生物量：</label>
                <input type="text" id="biomass" name="biomass" required><br><br>
                <input type="button" value="更新" onclick="calculateValue2()">
            </form>
        </div>
        
        <div id="output-value"></div>
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
                // var K = 13696000; // 此处需要从信息卡中提取K值
                var K = parseFloat({ K_value }); // Pass the value of K from the backend
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

            // JavaScript function to calculate the value
            function calculateValue1() {{
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

            // JavaScript function to calculate the value
            function calculateValue2() {{
                var year = parseFloat(document.getElementById("year").value);
                var biomass = parseFloat(document.getElementById("biomass").value);
                value = adjust_fishstate(year, biomass);

                var money = parseFloat({ money }); // Pass the value of money from the backend
                var outputElement = document.getElementById("output-value");
                if (value[0] === 0) {{
                    outputElement.innerHTML = "当前状态：可捕捞";
                }} else if (value[0] === 1) {{
                    outputElement.innerHTML = "当前状态：" + value[1] + "年后可捕捞";
                }} else if (value[0] === 2) {{
                    outputElement.innerHTML = "减少捕捞，预计经济收益为：" + value[1] * money;
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