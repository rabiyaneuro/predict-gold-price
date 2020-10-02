# -*- coding: utf-8 -*-

import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from pandas.plotting import autocorrelation_plot

import numpy as np

from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error

from scipy.optimize import differential_evolution

import warnings

#%% 
end_dt = '2020-07-17'
#importing gold futures closing prices from yahoo finance
data = yf.Ticker('GC=F').history(period="max").loc[:end_dt]['Close']

#%%

#autocorr
ax = autocorrelation_plot(data)
ax.set_xlim([0, 1750])

#%%

# fit model
model = ARIMA(data, order=(6,2,7))
model_fit = model.fit()
print(model_fit.summary())

# plot residual errors
residuals = pd.DataFrame(model_fit.resid)
residuals.plot()
plt.show()
residuals.plot(kind='kde')
plt.show()
print(residuals.describe())

#%%
X = data.loc['2020':]

def arima(X, arima_param, ifPrint = False):
    X = data.loc['2020':]

    # p = arima_param[0].astype(int)
    # d = arima_param[1].astype(int)
    # q = arima_param[2].astype(int)
    # print(p,d,q)
    
    size = int(len(X) * 0.66)
    train, test = X[0:size], X[size:len(X)]
    history = [x for x in train]
    
    predictions = list()
    for t in range(len(test)):
    	model = ARIMA(history, order=arima_param)
    	model_fit = model.fit(disp=0)
    	yhat = model_fit.forecast()[0]
    	predictions.append(yhat)
    	history.append(test[t])
        # if ifPrint:
        #     print('predicted=%f, expected=%f' % (yhat, test[t]))
    error = mean_squared_error(test, predictions)
        # if ifPrint:
        #     print('Test MSE: %.3f' % error)
    return error
#%% plot
plt.plot(test)
plt.plot(predictions, color='red')
plt.show()

#%% param search
bounds = np.array([[0,10], [0,2], [0,10]])

from geneticalgorithm import geneticalgorithm as ga


model=ga(function=arima,
         dimension=3,
         variable_type='int',
         variable_boundaries=bounds,
         function_timeout = 20)

model.run()

#%%
# # evaluate an ARIMA model for a given order (p,d,q)
# def evaluate_arima_model(X, arima_order):
# 	# prepare training dataset
# 	train_size = int(len(X) * 0.66)
# 	train, test = X[0:train_size], X[train_size:]
# 	history = [x for x in train]
# 	# make predictions
# 	predictions = list()
# 	for t in range(len(test)):
# 		model = ARIMA(history, order=arima_order)
# 		model_fit = model.fit(disp=0)
# 		yhat = model_fit.forecast()[0]
# 		predictions.append(yhat)
# 		history.append(test[t])
# 	# calculate out of sample error
# 	error = mean_squared_error(test, predictions)
# 	return error

# evaluate combinations of p, d and q values for an ARIMA model
def evaluate_models(dataset, p_values, d_values, q_values):
	dataset = dataset.astype('float32')
	best_score, best_cfg = float("inf"), None
	for p in p_values:
		for d in d_values:
			for q in q_values:
				order = (p,d,q)
				try:
					mse = arima(dataset, order)
					if mse < best_score:
						best_score, best_cfg = mse, order
					print('ARIMA%s MSE=%.3f' % (order,mse))
				except:
					continue
	print('Best ARIMA%s MSE=%.3f' % (best_cfg, best_score))

# evaluate parameters
p_values = [0, 1, 2, 4, 6, 8, 10]
d_values = range(0, 3)
q_values = range(0, 3)
warnings.filterwarnings("ignore")
evaluate_models(X, p_values, d_values, q_values)