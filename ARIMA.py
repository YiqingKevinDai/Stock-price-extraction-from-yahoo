# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 23:13:34 2018

ARIMA

@author: kevindai
"""

import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
df = pd.read_csv('monthly-milk-production-pounds-p.csv')

#Clean Up
df.columns = ['Month','Milk in pounds per cow']
df.head()

# Weird last value at bottom causing issues
df.drop(168,axis=0,inplace=True)

df['Month'] = pd.to_datetime(df['Month'])
df.set_index('Month',inplace=True)
df.describe().transpose()

#Visualize the Data
df.plot()
timeseries = df['Milk in pounds per cow']

timeseries.rolling(12).mean().plot(label='12 Month Rolling Mean')
timeseries.rolling(12).std().plot(label='12 Month Rolling Std')
timeseries.plot()
plt.legend()

timeseries.rolling(12).mean().plot(label='12 Month Rolling Mean')
timeseries.plot()
plt.legend()

#Decomposition
from statsmodels.tsa.seasonal import seasonal_decompose
decomposition = seasonal_decompose(df['Milk in pounds per cow'], freq=12)  
fig = plt.figure()  
fig = decomposition.plot()  
fig.set_size_inches(15, 8)

#Testing for Stationarity
from statsmodels.tsa.stattools import adfuller
result = adfuller(df['Milk in pounds per cow'])


print('Augmented Dickey-Fuller Test:')
labels = ['ADF Test Statistic','p-value','#Lags Used','Number of Observations Used']

for value,label in zip(result,labels):
    print(label+' : '+str(value) )
    
if result[1] <= 0.05:
    print("strong evidence against the null hypothesis, reject the null hypothesis. Data has no unit root and is stationary")
else:
    print("weak evidence against null hypothesis, time series has a unit root, indicating it is non-stationary ")


# Store in a function for later use!
def adf_check(time_series):
    """
    Pass in a time series, returns ADF report
    """
    result = adfuller(time_series)
    print('Augmented Dickey-Fuller Test:')
    labels = ['ADF Test Statistic','p-value','#Lags Used','Number of Observations Used']

    for value,label in zip(result,labels):
        print(label+' : '+str(value) )
    
    if result[1] <= 0.05:
        print("strong evidence against the null hypothesis, reject the null hypothesis. Data has no unit root and is stationary")
    else:
        print("weak evidence against null hypothesis, time series has a unit root, indicating it is non-stationary ")

adf_check(df['Milk in pounds per cow'])

#Differencing
df['Milk First Difference'] = df['Milk in pounds per cow'] - df['Milk in pounds per cow'].shift(1)
adf_check(df['Milk First Difference'].dropna())
df['Milk First Difference'].plot()

#Second Difference 
df['Milk Second Difference'] = df['Milk First Difference'] - df['Milk First Difference'].shift(1)
adf_check(df['Milk Second Difference'].dropna())
df['Milk Second Difference'].plot()

#Seasonal First Difference 
# You can also do seasonal first difference
df['Seasonal First Difference'] = df['Milk First Difference'] - df['Milk First Difference'].shift(12)
df['Seasonal First Difference'].plot()
adf_check(df['Seasonal First Difference'].dropna())

#Autocorrelation
from statsmodels.graphics.tsaplots import plot_acf,plot_pacf
fig_first = plot_acf(df["Milk First Difference"].dropna())

fig_seasonal_first = plot_acf(df["Seasonal First Difference"].dropna())

from pandas.plotting import autocorrelation_plot
autocorrelation_plot(df['Seasonal First Difference'].dropna())

#Using the Seasonal ARIMA model
For non-seasonal data
from statsmodels.tsa.arima_model import ARIMA

# We have seasonal data!
model = sm.tsa.statespace.SARIMAX(df['Milk in pounds per cow'],order=(0,1,0), seasonal_order=(1,1,1,12))
results = model.fit()
print(results.summary())
      
      
#Prediction of Future Values
df['forecast'] = results.predict(start = 150, end= 168, dynamic= True)  
df[['Milk in pounds per cow','forecast']].plot(figsize=(12,8))

from pandas.tseries.offsets import DateOffset
future_dates = [df.index[-1] + DateOffset(months=x) for x in range(0,24) ]

future_dates

future_dates_df = pd.DataFrame(index=future_dates[1:],columns=df.columns)

future_df = pd.concat([df,future_dates_df])

future_df.head()

future_df['forecast'] = results.predict(start = 168, end = 188, dynamic= True)  
future_df[['Milk in pounds per cow', 'forecast']].plot(figsize=(12, 8)) 







