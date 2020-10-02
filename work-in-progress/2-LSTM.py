# -*- coding: utf-8 -*-

#%% load dataset


"""
Tickers being used:
gold futures
SPDR GLD - gold investment fund
Barrick Gold Corporation (mining)

usd currency index
S&p500
dow jones
NASDAQ Composite
S&P/TSX Composite index
"""

tickers = {'GC=F': 'Gold Futures',
           'GLD' : 'Gold Investment Fund',
           'GOLD': 'Barrick Gold (mining)',
           'DX-Y.NYB?P=DX-Y.NYB': 'USD Currency Index',
           '^GSPC':'S&P500',
           '^DJI': 'Dow Jones',
           '^IXIC': 'NASDAQ Composite',
           '^GSPTSE'}

res = []     
for t in tickers:
    temp = yf.Ticker(t).history(period="max")['Close'].loc['2000':]
    temp.rename(t, inplace = True)
    res.append(temp)

all_close = pd.concat(res, axis = 1)