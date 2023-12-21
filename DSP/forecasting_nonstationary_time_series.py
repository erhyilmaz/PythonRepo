"""

Challenges of Non-Stationary Time Series
Non-stationary time series, on the other hand, exhibit changing statistical properties over time.
This makes them more challenging to work with and forecast. The main challenges associated with non-stationary time series are:

1- Trend: Non-stationary data often displays a trend, which is a long-term systematic movement in one direction,
either upward (an increasing trend) or downward (a decreasing trend).
Identifying and removing the trend is crucial for forecasting.

2- Seasonality: Seasonality is another common characteristic of non-stationary data.
It represents periodic fluctuations that occur at regular intervals, such as daily, monthly, or yearly patterns.
Accounting for seasonality is vital in making accurate forecasts.

3- Heteroscedasticity: Non-stationary time series often exhibit varying levels of volatility or variance over time.
This heteroscedasticity can make it difficult to develop forecasting models that assume constant variance.
-------------------------------

AutoRegressive Integrated Moving Average (ARIMA) models are widely used for non-stationary time series.
ARIMA models involve differencing the data to make it stationary and then
modeling it using autoregressive and moving average components.

Forecasting non-stationary time series typically involves a series of steps,
including data preprocessing, model selection, training, and plotting the results.
Here’s a Python code example for forecasting a non-stationary time series using the ARIMA model with a dataset and plots:
"""


# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import adfuller

# Generate or load a non-stationary time series dataset
# For demonstration, we'll generate a simple non-stationary dataset
np.random.seed(42)

# Generate a non-stationary time series with a trend and seasonality
t = np.arange(1, 101)
seasonal_component = 10 * np.sin(0.2 * t)
trend_component = 0.5 * t
noise = np.random.normal(0, 2, 100)
data = seasonal_component + trend_component + noise

# Create a pandas DataFrame from the dataset
df = pd.DataFrame({'Data': data})

# Plot the original time series data
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['Data'], label='Original Data')
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Non-Stationary Time Series Data')
plt.legend()
plt.show()

# Check for stationarity using Augmented Dickey-Fuller test
def adf_test(series):
    result = adfuller(series)
    print('ADF Statistic:', result[0])
    print('p-value:', result[1])
    print('Critical Values:', result[4])

adf_test(df['Data'])

# Differencing to make the time series stationary
df['Differenced_Data'] = df['Data'] - df['Data'].shift(1)
df = df.dropna()

# Plot the differenced time series data
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['Differenced_Data'], label='Differenced Data')
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Stationary Time Series Data')
plt.legend()
plt.show()

# ACF and PACF plots for determining ARIMA orders
plt.figure(figsize=(12, 6))
plot_acf(df['Differenced_Data'], lags=20, ax=plt.gca())
plt.title('ACF Plot')
plt.show()

plt.figure(figsize=(12, 6))
plot_pacf(df['Differenced_Data'], lags=20, ax=plt.gca())
plt.title('PACF Plot')
plt.show()

# Split the data into training and testing sets
train_size = int(0.8 * len(df))
train, test = df['Differenced_Data'][:train_size], df['Differenced_Data'][train_size:]

# Fit an ARIMA model to the training data
model = ARIMA(train, order=(1, 1, 1))
model_fit = model.fit()

# Forecast the test data
forecast = model_fit.forecast(steps=len(test))

# Calculate prediction intervals
residuals = test - forecast
prediction_interval = 1.96 * np.std(residuals)  # 1.96 for a 95% prediction interval

# Plot the forecasts and the actual values with prediction intervals
plt.figure(figsize=(12, 6))
plt.plot(df.index[train_size:], test, label='Actual')
plt.plot(df.index[train_size:], forecast, label='Forecast', color='red')
plt.fill_between(df.index[train_size:], forecast - prediction_interval, forecast + prediction_interval, color='pink', alpha=0.3)
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('ARIMA Forecasting with Prediction Intervals')
plt.legend()
plt.show()