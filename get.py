import requests
import pandas as pd

# 使用你的 API 密钥
api_key = '6ZI495EUNAXCLI7T'

# 请求 URL
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey={api_key}'

# 发起请求
r = requests.get(url)

# 解析返回的 JSON 数据
data = r.json()

# 获取时间序列数据
time_series = data.get('Time Series (5min)', {})

# 如果有数据，转换为 DataFrame
if time_series:
    df = pd.DataFrame.from_dict(time_series, orient='index')
    df = df.astype(float)  # 将数据转换为浮动数字
    
    # 显示数据
    print(df.head())  # 显示前几行数据
else:
    print("未获取到有效数据")
