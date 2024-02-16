import pandas as pd 
# To visualize the results 
import matplotlib.pyplot as plt
import seaborn

from yahooquery import Ticker

symbols_list = [
    "^BVSP", # IBOVESPA
    "^GSPC", # S&P 500
    "^FVX", # Treasury Yield 5 Years
    "^TYX", # Treasury Yield 30 Years
    "BTC-USD",
    "BITH11.SA",
    "GOLD11.SA",
]

tickers = Ticker(" ".join(symbols_list))
df = tickers.history(period='max')
df = df.reset_index()
df = df[['date', 'adjclose', 'symbol']]
df_pivot=df.pivot(index='date', columns='symbol', values='adjclose').reset_index(drop=True)

corr_df = df_pivot.corr(method='pearson')

plt.figure(figsize=(13, 8))
seaborn.heatmap(corr_df, annot=True, cmap='RdYlGn')
plt.show()
