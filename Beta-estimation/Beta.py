## in this project we will try to estimate Oklahoma Christian Univeristy stock portfolio beta

from os import stat, statvfs
import pandas as pd
import pandas_datareader as pdr
import yfinance as yf
import numpy as np
import datetime as dt
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import norm
import seaborn as sns

# Create a list of tickers and weights
tickers = ['ACI', 'AAPL' ,'AZO' ,'BRK-B' ,'BA' ,'CHGG' ,'CSCO', 'CCI', 'CVS' ,'DVN' ,'DG',
 'EPD' ,'EQIX' ,'XOM' ,'GS' ,'HA', 'HD' ,'JNJ', 'LDOS' ,'MMP' ,'MARA' ,'MCD' ,'MU',
 'PINS', 'PAA', 'PSA', 'RIOT' ,'RPRX' ,'LUV' ,'SIVB' ,'TDOC' ,'TXT' ,'TMDX', 'UL',
 'U' ,'V', 'WMT' ,'DRIV' ,'SDIV' ,'EEM', 'IDRV']

wts = np.array([0.0231, 0.0244, 0.0261, 0.0213, 0.0258, 0.0111, 0.0415, 0.0449 ,0.0371, 0.0145,
 0.0277 ,0.0239 ,0.0203, 0.018 , 0.0279, 0.0315,0.0208, 0.0278 ,0.0232, 0.005,
 0.0073 ,0.0251, 0.0292, 0.0131, 0.0148 ,0.0201, 0.0056,0.0259, 0.0131 ,0.0284,
 0.0161, 0.045 , 0.0204, 0.0174, 0.0127, 0.0101, 0.0343 ,0.0166 ,0.0182 ,0.0201,
 0.0165])

data = pdr.get_data_yahoo(tickers, start="2011-01-01", end=dt.date.today())['Adj Close']

#print (data)

ret_data = data.pct_change()[1:]

port_ret = (ret_data * wts).sum(axis = 1)


benchmark_price = pdr.get_data_yahoo('SPY', start="2011-01-01", end=dt.date.today())

benchmark_ret = benchmark_price["Adj Close"].pct_change()[1:]

sns.regplot(benchmark_ret.values,
port_ret.values)
plt.xlabel("Benchmark Returns")
plt.ylabel("Portfolio Returns")
plt.title("Portfolio Returns vs Benchmark Returns")
plt.show()

(beta, alpha) = stats.linregress(benchmark_ret.values,
                port_ret.values)[0:2]
                
print("The portfolio beta is", round(beta, 4))
print("The portfolio beta is", round(alpha,5))


