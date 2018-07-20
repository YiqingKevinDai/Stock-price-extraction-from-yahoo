import pandas as pd
import quandl
start = pd.to_datetime('2012-01-01')
end = pd.to_datetime('2017-01-01')

# Grabbing a bunch of tech stocks for our portfolio
aapl = quandl.get('WIKI/AAPL.11',start_date=start,end_date=end)
cisco = quandl.get('WIKI/CSCO.11',start_date=start,end_date=end)
ibm = quandl.get('WIKI/IBM.11',start_date=start,end_date=end)
amzn = quandl.get('WIKI/AMZN.11',start_date=start,end_date=end)

# Alternative
# aapl = pd.read_csv('AAPL_CLOSE',index_col='Date',parse_dates=True)
# cisco = pd.read_csv('CISCO_CLOSE',index_col='Date',parse_dates=True)
# ibm = pd.read_csv('IBM_CLOSE',index_col='Date',parse_dates=True)
# amzn = pd.read_csv('AMZN_CLOSE',index_col='Date',parse_dates=True)

aapl.to_csv('AAPL_CLOSE')
cisco.to_csv('CISCO_CLOSE')
ibm.to_csv('IBM_CLOSE')
amzn.to_csv('AMZN_CLOSE')

# cumulative daily returns
for stock_df in (aapl,cisco,ibm,amzn):
    stock_df['Normed Return'] = stock_df['Adj. Close']/stock_df.iloc[0]['Adj. Close']
#Allocations
"""
30% in Apple
20% in Google/Alphabet
40% in Amazon
10% in IBM
"""

for stock_df,allo in zip([aapl,cisco,ibm,amzn],[.3,.2,.4,.1]):
    stock_df['Allocation'] = stock_df['Normed Return']*allo
    
#Let's pretend we invested a million dollars in this portfolio   
for stock_df in [aapl,cisco,ibm,amzn]:
    stock_df['Position Values'] = stock_df['Allocation']*1000000
    
#Total Portfolio Value
portfolio_val = pd.concat([aapl['Position Values'],cisco['Position Values'],ibm['Position Values'],amzn['Position Values']],axis=1)

portfolio_val.columns = ['AAPL Pos','CISCO Pos','IBM Pos','AMZN Pos']

import matplotlib.pyplot as plt

portfolio_val['Total Pos'].plot(figsize=(10,8))
plt.title('Total Portfolio Value')

portfolio_val.drop('Total Pos',axis=1).plot(kind='line')

#Daily Returns
portfolio_val['Daily Return'] = portfolio_val['Total Pos'].pct_change(1)

#Cumulative Return
cum_ret = 100 * (portfolio_val['Total Pos'][-1]/portfolio_val['Total Pos'][0] -1 )
print('Our return {} was percent!'.format(cum_ret))

#Avg Daily Return
portfolio_val['Daily Return'].mean()

#Std Daily Return
portfolio_val['Daily Return'].std()
portfolio_val['Daily Return'].plot(kind='kde')

#Sharpe Ratio
SR = portfolio_val['Daily Return'].mean()/portfolio_val['Daily Return'].std()
ASR = (252**0.5)*SR
portfolio_val['Daily Return'].std()
portfolio_val['Daily Return'].mean()
portfolio_val['Daily Return'].plot('kde')












    
