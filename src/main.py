from pandas_datareader import data as pdr
import yfinance as yfin

yfin.pdr_override()

petr4_df = pdr.get_data_yahoo('PETR4.SA', start='2022-10-24', end='2022-12-23')
print("petr4_df.head: {}".format(petr4_df.head()))
print("petr4_df.tail: {}".format(petr4_df.tail()))
