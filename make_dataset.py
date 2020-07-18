# -*- coding: utf-8 -*-
"""
Downloading the dataset
"""

import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#%%

end_dt = '2020-07-17'
future_dt = '2020-07-24'


# we have training data until July 10 because the 
# predicted price for that is July 17
#TODO: when do we start collecting data from?

#%% 
"""
gold futures
SPDR GLD - gold investment fund
Barrick Gold Corporation (mining)

usd currency index
S&p500
dow jones
S&P/TSX Composite index

"""
tickers = ["GC=F",
           "GLD",
           "^GSPC",
           "GOLD",
           "DX-Y.NYB?P=DX-Y.NYB",
           "^DJI",
           "^IXIC",
           "^GSPTSE"
           ]

#gather 'close' values for each     
res = []     
for t in tickers:
    temp = yf.Ticker(t).history(period="max")['Close'].loc['2000':]
    temp.rename(t, inplace = True)
    res.append(temp)

all_close = pd.concat(res, axis = 1)

# subplots
axes = all_close.loc['2020':].plot(marker='.', alpha=0.5, linestyle='None', 
                      figsize=(11, 9), subplots=True)


#%%

# gold futures
gcf = yf.Ticker("GC=F").history(period="max")
gcf = gcf.loc[:end_dt]

#SPDR
spdr = yf.Ticker("GLD").history(period="max")



#TODO: create training and test sets
# y - predicted future close price gcf
# x all the feature closing values 7 days prior
#%% Initial data explore and viz

# plot all stacked
