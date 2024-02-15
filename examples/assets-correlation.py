import pandas as pd 
# To visualize the results 
import matplotlib.pyplot as plt
import seaborn

from yahooquery import Ticker

symbols_list = [
    "IVVB11.SA",
    "BITH11.SA",
    "BOVA11.SA",
    "^GSPC", # S&P 500
    "^FVX", # Treasury Yield 5 Years
    "^TYX", # Treasury Yield 30 Years
    "BTC-USD",
]

tickers = Ticker(" ".join(symbols_list))
df = tickers.history()
df = df.reset_index()
df = df[['date', 'close', 'symbol']]
df_pivot=df.pivot(index='date', columns='symbol', values='close').reset_index(drop=True)

corr_df = df_pivot.corr(method='pearson')

plt.figure(figsize=(13, 8))
seaborn.heatmap(corr_df, annot=True, cmap='RdYlGn')
plt.show()
