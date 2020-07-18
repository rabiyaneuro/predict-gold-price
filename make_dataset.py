# -*- coding: utf-8 -*-
"""
Downloading the dataset
"""

import yfinance as yf

#%% import the data from yahoo finance

# gold futures
gcf = yf.Ticker("GC=F")
gcf = gcf.history(period="max")

# USD currency

#Gold ETF

#Jewellry stock 

#%%