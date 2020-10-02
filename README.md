# predict-gold-price

Task: Predict the price of gold at market close on Friday July 24, 2020

Solution consists of:
- initial-data-explore.ipynb - initial exploration and some visualizations of data
- ARIMA.ipynb - fitting ARIMA model on gold prices and some visualizations

Final Answer: $1813.56

Assumptions and Notes:

- Gold Aug 20 Future is proxy for ‘price of gold’ (which I interpreted as spot price of gold)
  - In reality these prices can differ by a significant amount however I was using the Yahoo Finance API and they don’t provide the spot price of gold
  - If I had more time I would use another API that offers more reliable financial data or write a script to scrape a website for the spot price of gold

- Used recent data only (data from 2020) to save time when tuning hyperparameters and also since a lot of changes occurred in the economy this year due to the pandemic, so I focused on this year’s dynamics
  - With more time, I would use more than just this year’s data but account for the effects of the pandemic when modelling

- Developed a model that forecast 7 days into future
  - Used training data up until July 17, 2020 to get July 24 forecast

- I used ARIMA which is a univariate time series technique as a simple starting point to see what prediction I would get
  - There are definitely other factors that affect gold price which is why this model worked poorly, and I explore in initial-data-explore.ipynb, so with more time I would try multivariate time series modelling techniques or sequence models (RNN, LSTM etc.)
