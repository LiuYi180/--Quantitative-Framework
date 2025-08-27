import pandas as pd

# 初始化参数
window = 20  # 布林带计算的窗口大小
std_multiplier = 2  # 标准差的倍数

# 存储价格数据
price_data = pd.Series()
# 存储上一个时间点的布林带信息
last_boll_mid = None
last_boll_upper = None
last_boll_lower = None
# 存储上一个信号
last_signal = None

#    参数:
#       time: 当前时间
#       price: 当前价格
#   返回:
#       "做多": 买入信号
#       "做空": 卖出信号
 #      "平多": 平多仓信号
 #      "平空": 平空仓信号
 #     "不操作": 不操作信号




def trade_signal(time, price):    #核心函数代码，必须要有这个，框架里会调用，只能传入time和price，没有vol，需要的话自己改框架
    
    global price_data, last_boll_mid, last_boll_upper, last_boll_lower, last_signal

    # 添加新的价格数据
    price_data = pd.concat([price_data, pd.Series([price])])

    # 计算布林带
    if len(price_data) >= window:
        boll_mid = price_data.rolling(window=window).mean()
        boll_std = price_data.rolling(window=window).std()
        boll_upper = boll_mid + std_multiplier * boll_std
        boll_lower = boll_mid - std_multiplier * boll_std

        current_boll_mid = boll_mid.iloc[-1]
        current_boll_upper = boll_upper.iloc[-1]
        current_boll_lower = boll_lower.iloc[-1]

        # 交易信号逻辑
        if last_boll_mid is not None:
            if price > current_boll_upper and price < last_boll_upper:
                signal = "平多" if last_signal == "做多" else None
            elif price < current_boll_lower and price > last_boll_lower:
                signal = "平空" if last_signal == "做空" else None
            elif price > current_boll_mid and price < current_boll_upper:
                signal = "做多"
            elif price < current_boll_mid and price > current_boll_lower:
                signal = "做空"
            else:
                signal = None

            if signal:
                last_signal = signal
            return signal

        last_boll_mid = current_boll_mid
        last_boll_upper = current_boll_upper
        last_boll_lower = current_boll_lower

    return None
