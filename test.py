# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 10:12:32 2021

@author: Jason
"""

import requests
import pandas as pd
import matplotlib as plt
url = "https://api.finmindtrade.com/api/v4/data"
parameter = {
    "dataset": "TaiwanStockPrice",
    "data_id": "2330",
    "start_date": "2007-01-01",
    "end_date": "2020-10-31",
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkYXRlIjoiMjAyMS0xMS0wMSAwOTo1OTozOSIsInVzZXJfaWQiOiJscGxkMTEyMiIsImlwIjoiMTQwLjExMC4yMTUuMjE0In0.BPn9QqKH8oX9uuN90C6uXMp7Z1VN5vcdA72FfyBnYBc", # 參考登入，獲取金鑰
}
resp = requests.get(url, params=parameter)
data = resp.json()
data = pd.DataFrame(data["data"])
print(data.head())
plt.plot(data.date,data.open)


import requests
import pandas as pd
url = "https://api.finmindtrade.com/api/v4/data"

parameter = {
    "dataset": "TaiwanStockPER",
    "data_id": "2330",
    "start_date": "2020-10-31",
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkYXRlIjoiMjAyMS0xMS0wMSAwOTo1OTozOSIsInVzZXJfaWQiOiJscGxkMTEyMiIsImlwIjoiMTQwLjExMC4yMTUuMjE0In0.BPn9QqKH8oX9uuN90C6uXMp7Z1VN5vcdA72FfyBnYBc", # 參考登入，獲取金鑰
}
data = requests.get(url, params=parameter)
data = data.json()
data = pd.DataFrame(data['data'])
print(data.head())

# 取得股價
from FinMind.data import DataLoader

dl = DataLoader()
# 下載台股股價資料
stock_data = dl.taiwan_stock_daily(
stock_id='2609', start_date='2018-01-01', end_date='2021-06-26'
)
# 下載三大法人資料
stock_data = dl.feature.add_kline_institutional_investors(
stock_data
) 
# 下載融資券資料
stock_data = dl.feature.add_kline_margin_purchase_short_sale(
stock_data
)

# 繪製k線圖
from FinMind import plotting

plotting.kline(stock_data)