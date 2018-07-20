# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 22:22:12 2018

Introduction to Statsmodels

@author: kevindai
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import statsmodels.api as sm

df = sm.datasets.macrodata.load_pandas().data

print(sm.datasets.macrodata.NOTE)

index = pd.Index(sm.tsa.datetools.dates_from_range('1959Q1', '2009Q3'))

df.index = index

df['realgdp'].plot()
plt.ylabel("REAL GDP")

#Using Statsmodels to get the trend
gdp_cycle, gdp_trend = sm.tsa.filters.hpfilter(df.realgdp)
df["trend"] = gdp_trend
df[['trend','realgdp']].plot()

df[['trend','realgdp']]["2000-03-31":].plot(figsize=(12,8))

