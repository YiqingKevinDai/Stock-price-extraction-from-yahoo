# Model CAPM as a simple linear regression
from scipy import stats
import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt


spy_etf = web.DataReader('SPY','google')

start = pd.to_datetime('2010-01-04')
end = pd.to_datetime('2017-07-18')
aapl = web.DataReader('AAPL','google',start,end)

aapl['Close'].plot(label='AAPL',figsize=(10,8))
spy_etf['Close'].plot(label='SPY Index')
plt.legend()

#Get Daily Return
aapl['Daily Return'] = aapl['Close'].pct_change(1)
spy_etf['Daily Return'] = spy_etf['Close'].pct_change(1)

#regression
beta,alpha,r_value,p_value,std_err = stats.linregress(aapl['Daily Return'].iloc[1:],spy_etf['Daily Return'].iloc[1:])

beta

alpha

r_value


