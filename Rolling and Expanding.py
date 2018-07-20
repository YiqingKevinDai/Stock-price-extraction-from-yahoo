# -*- coding: utf-8 -*-
"""
Rolling and Expanding

Created on Fri Jul 20 17:30:45 2018

@author: kevindai
"""

import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

# Best way to read in data with time series index!
df = pd.read_csv('C:/Users/kevindai/Python-for-Finance-Repo-master/09-Python-Finance-Fundamentals/walmart_stock.csv',index_col='Date',parse_dates=True)

df['Open'].plot(figsize=(16,6))
# 7 day rolling mean
df.rolling(7).mean().head(20)

df['Open'].plot()
df.rolling(window=30).mean()['Close'].plot()

df['Close'].rolling(window=30).mean().plot(figsize=(16,6))

df['Close: 30 Day Mean'] = df['Close'].rolling(window=30).mean()
df[['Close','Close: 30 Day Mean']].plot(figsize=(16,6))

#expanding
df['Close'].expanding(min_periods=1).mean().plot(figsize=(16,6))

#Bollinger Bands

df['Close: 30 Day Mean'] = df['Close'].rolling(window=20).mean()
df['Upper'] = df['Close: 30 Day Mean'] + 2*df['Close'].rolling(window=20).std()
df['Lower'] = df['Close: 30 Day Mean'] - 2*df['Close'].rolling(window=20).std()
df[['Close','Close: 30 Day Mean','Upper','Lower']].plot(figsize=(16,6))