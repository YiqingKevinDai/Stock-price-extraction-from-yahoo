# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 23:00:54 2018

@author: kevindai
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# To illustrate the order of arguments
my_year = 2016
my_month = 1
my_day = 2
my_hour = 13
my_minute = 30
my_second = 15

# January 2nd, 2017
my_date = datetime(my_year,my_month,my_day)

# January 2nd, 2017 at 13:30:15
my_date_time = datetime(my_year,my_month,my_day,my_hour,my_minute,my_second)

first_two = [datetime(2016, 1, 1), datetime(2016, 1, 2)]

dt_ind = pd.DatetimeIndex(first_two)
dt_ind

# Attached to some random data
data = np.random.randn(2,2)
print(data)
cols = ['A','B']

df = pd.DataFrame(data,dt_ind,cols)

# Latest Date Location
df.index.argmax()

# Grab data
# Faster alternative
# df = pd.read_csv('time_data/walmart_stock.csv',index_col='Date')
df = pd.read_csv('C:/Users/kevindai/Python-for-Finance-Repo-master/05-Pandas-with-Time-Series/time_data/walmart_stock.csv')

df['Date'] = pd.to_datetime(df['Date'])

df.set_index('Date',inplace=True)

df.head()

df.index

df.resample(rule='M', convention='end').head()
# Yearly Means
df.resample(rule='A').mean()

df['Close'].resample('A').mean().plot(kind='bar')
plt.title('Yearly Mean Close Price for Walmart')

df['Open'].plot(figsize=(16,6))

df['Close'].plot()
df.rolling(window=30).mean()['Close'].plot()

# take the end of annual data as a new dataframe ****
df5 = df.resample(rule='A', convention='end').mean()
df5.head()
