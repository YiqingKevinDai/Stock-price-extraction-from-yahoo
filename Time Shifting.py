# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 20:47:47 2018

@author: kevindai
"""

import pandas as pd

import matplotlib.pyplot as plt
%matplotlib inline

df = pd.read_csv('time_data/walmart_stock.csv',index_col='Date')
df.index = pd.to_datetime(df.index)

#shift() forward
df.shift(1).head()

#shift() backwards
df.shift(-1).head()

# Shift everything forward one month
df.tshift(periods=1,freq='M').head()
