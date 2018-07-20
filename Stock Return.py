#Daily Return
start = datetime.datetime(2012, 1, 1)
end = datetime.datetime(2017, 1, 1)
tesla = web.DataReader("TSLA", 'google', start, end)

tesla['returns'] = (tesla['Close'] / tesla['Close'].shift(1) ) - 1
tesla['returns'] = tesla['Close'].pct_change(1)

# Cumulative Return

tesla['Cumulative Return'] = (1 + tesla['returns']).cumprod()

tesla['Cumulative Return'].plot(label='Tesla',figsize=(16,8),title='Cumulative Return')
