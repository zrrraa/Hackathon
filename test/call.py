import math


def calculate_fishstate(year, biomass1,
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


def adjust_fishstate(year, biomass):  #year用户输入年 biomass生物量 用于图1/2/3
    K = 13696000  #此处需要从信息卡中提取K值 ！！！！！
    intrinsic_growth_rate = 0.53
    if biomass >= K / 2:
        return 0, 0  #若可捕捞则返回[0,0]

    result = transcendental_equation(K, biomass, intrinsic_growth_rate)
    if result >= 1:
        return 1, (year + result - 2023)  #若禁渔则返回[1,禁渔时间]
    else:
        return 2, K / 2 - biomass  #若减少捕捞则返回[2,经济收益]  此处经济收益是（K/2-biomass）*money ！！！！


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