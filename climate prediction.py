import pandas as pd
from statsmodels.tsa.arima_model import ARIMA

# Load data
df = pd.read_csv('weather.csv', parse_dates=['date'], index_col='date')

# Assume we are predicting 'temperature'
temp_df = df['temperature']

# Build and Train Model
model = ARIMA(temp_df, order=(5,1,0)) # The order parameters must be adjusted according to your specific use case
model_fit = model.fit(disp=0)

# Overview of the model
print(model_fit.summary())

# Predict climate
forecast = model_fit.forecast(steps=10) # predicts the next 10 days weather
print(forecast)
