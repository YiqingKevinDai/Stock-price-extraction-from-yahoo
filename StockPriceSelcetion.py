# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 14:05:50 2018

1.Functions from St.data and pandas_datareader.wb extract data from various Internet sources into a pandas DataFrame. 
2.Select dataframe rows between two dates
3.Moving Averages
4.Visulization
@author: kevindai
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Pandas Datareader

import pandas_datareader.data as wb
import datetime 
start = datetime.datetime(2012, 1, 1)
end = datetime.datetime(2017, 1, 1)

tesla = wb.DataReader('TSLA', 'yahoo', start, end)
ford = wb.DataReader('F', 'yahoo', start, end)
gm = wb.DataReader('GM', 'yahoo', start, end)

tesla.to_csv('Tesla_Stock.csv')
ford.to_csv('Ford_Stock.csv')
gm.to_csv('GM_Stock.csv')

tesla['Open'].plot(label='Tesla',figsize=(16,8),title='Open Price')
gm['Open'].plot(label='GM')
ford['Open'].plot(label='Ford')
plt.legend()


ford['Volume'].argmax()

#Select dataframe rows between two dates
"""
Using a boolean mask:
df = pd.DataFrame(np.random.random((200,3)))
df['date'] = pd.date_range('2000-1-1', periods=200, freq='D')
mask = (df['date'] > '2000-6-1') & (df['date'] <= '2000-6-10')
print(df.loc[mask])

Using a DatetimeIndex:
df = pd.DataFrame(np.random.random((200,3)))
df['date'] = pd.date_range('2000-1-1', periods=200, freq='D')
df = df.set_index(['date'])
print(df.loc['2000-6-1':'2000-6-10'])    
"""
gm.loc[gm.index < '2012-1-11']
gm['2012-1-11': '2012-1-15']

#Plot this "Total Traded" against the time index.
tesla['Total Traded'] = tesla['Open']*tesla['Volume']
ford['Total Traded'] = ford['Open']*ford['Volume']
gm['Total Traded'] = gm['Open']*gm['Volume']

tesla['Total Traded'].plot(label='Tesla',figsize=(16,8))
gm['Total Traded'].plot(label='GM')
ford['Total Traded'].plot(label='Ford')
plt.legend()
plt.ylabel('Total Traded')

#
#practice plotting out some MA (Moving Averages). Plot out the MA50 and MA200 for GM. 
gm['MA50'] = gm['Open'].rolling(50).mean()
gm['MA200'] = gm['Open'].rolling(200).mean()
gm[['Open','MA50','MA200']].plot(label='gm',figsize=(16,8))

#scatter matrix plot

from pandas.plotting import scatter_matrix
car_comp = pd.concat([tesla['Open'], gm['Open'], ford['Open']], axis = 1)
car_comp.columns = ['Tesla Open','GM Open','Ford Open']

scatter_matrix(car_comp,figsize=(8,8),alpha=0.2,hist_kwds={'bins':50})

# Visualization Task 

from matplotlib.finance import candlestick_ohlc
from matplotlib.dates import DateFormatter, date2num, WeekdayLocator, DayLocator, MONDAY

# Rest the index to get a column of January Dates
ford_reset = ford.loc['2012-01':'2012-01'].reset_index()

# Create a new column of numerical "date" values for matplotlib to use
ford_reset['date_ax'] = ford_reset['Date'].apply(lambda date: date2num(date))
ford_values = [tuple(vals) for vals in ford_reset[['date_ax', 'Open', 'High', 'Low', 'Close']].values]

mondays = WeekdayLocator(MONDAY)        # major ticks on the mondays
alldays = DayLocator()              # minor ticks on the days
weekFormatter = DateFormatter('%b %d')  # e.g., Jan 12
dayFormatter = DateFormatter('%d')      # e.g., 12

#Plot it
fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2)
ax.xaxis.set_major_locator(mondays)
ax.xaxis.set_minor_locator(alldays)
ax.xaxis.set_major_formatter(weekFormatter)

candlestick_ohlc(ax, ford_values, width=0.6, colorup='g',colordown='r');

#Daily Percentage Change
tesla['returns'] = tesla['Close'].pct_change(1)
ford['returns'] = ford['Close'].pct_change(1)
gm['returns'] = gm['Close'].pct_change(1)

tesla['returns'].hist(bins=100,label='Tesla',figsize=(10,8),alpha=0.5)
gm['returns'].hist(bins=100,label='GM',alpha=0.5)
ford['returns'].hist(bins=100,label='Ford',alpha=0.5)
plt.legend()

tesla['returns'].plot(kind='kde',label='Tesla',figsize=(12,6))
gm['returns'].plot(kind='kde',label='GM')
ford['returns'].plot(kind='kde',label='Ford')
plt.legend()

