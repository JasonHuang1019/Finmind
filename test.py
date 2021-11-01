# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 10:12:32 2021

@author: Jason
"""

import requests
import pandas as pd
import matplotlib as plt
import mplfinance as mpf
 
url = "https://api.finmindtrade.com/api/v4/data"
parameter = {
    "dataset": "TaiwanStockPrice",
    "data_id": "2330",
    "start_date": "2020-01-01",
    "end_date": "2020-10-31",
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkYXRlIjoiMjAyMS0xMS0wMSAwOTo1OTozOSIsInVzZXJfaWQiOiJscGxkMTEyMiIsImlwIjoiMTQwLjExMC4yMTUuMjE0In0.BPn9QqKH8oX9uuN90C6uXMp7Z1VN5vcdA72FfyBnYBc", # 參考登入，獲取金鑰
}
resp = requests.get(url, params=parameter)
data = resp.json()
data = pd.DataFrame(data["data"])
print(data.head())
plot(data.open)


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



df = pd.DataFrame(data, columns = ['date', 'open','max','min','close','Trading_Volume'],)
df = df.set_index(pd.DatetimeIndex(df['date']))

df = df.rename(columns={'open': 'Open'})
df = df.rename(columns={'max': 'High'})
df = df.rename(columns={'min': 'Low'})
df = df.rename(columns={'close': 'Close'})
df = df.rename(columns={'Trading_Volume': 'Volume'})


mpf.plot(df,type='candle')


