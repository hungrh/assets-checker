#!/usr/bin/env python3

import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
from scipy.stats import norm

import yfinance as yfin

yfin.pdr_override()

start_date = "2015-01-01"
pg_df = wb.get_data_yahoo("PG", start=start_date)

data = pg_df["Adj Close"]
log_returns = np.log(1 + data.pct_change())

u = log_returns.mean()
var = log_returns.var()
drift = u - (0.5 * var)
stdev = log_returns.std()

print(f"u: {u}")
print(f"var: {var}")
print(f"drift: {drift}")
print(f"type: {type(drift)}")
print(f"stdev: {stdev}")
print(f"type: {type(stdev)}")

t_intervals = 365 * 8
iterations = 10

# price_today = price_yesterday * (e ^ r)
# - r is a random variable
# - Brownian motion is a concept that would allow us to model such randomness
# -- drift: u - (0.5 * var)
# -- random component: stdev * Z(rand(0;1))

daily_returns = np.exp(
    np.array(drift)
    + np.array(stdev) * norm.ppf(np.random.rand(t_intervals, iterations))
)
print(f"daily_returns: {daily_returns}")

#  NOTE(HRH):
# * -1 to forecasting from current day
# * 0 to forecasting from 2015-01-01

# S0 = data.iloc[-1]
S0 = data.iloc[0]
print(f"S0: {S0}")

price_list = np.zeros_like(daily_returns)
price_list[0] = S0
for t in range(1, t_intervals):
    price_list[t] = price_list[t - 1] * daily_returns[t]

## plotting data ##
fig, ((ax0, ax1), (ax2, ax3)) = plt.subplots(nrows=2, ncols=2, figsize=(15, 9))

ax0.plot(data)
ax0.set_title("Stock prices")

ax1.scatter(log_returns.index, log_returns.values)
ax1.set_title("Close price % changes")

ax2.hist(log_returns)
ax2.set_title("Histogram of close price % changes")

ax3.plot(price_list)
ax3.set_title(f"Monte carlo simulations from {start_date}")

fig.tight_layout()
plt.show()
