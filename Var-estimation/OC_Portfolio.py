## in this project we will try to estimate the Value at risk oklahoma Christian's stock portfolio
## Based on their historical market data.





import pandas as pd
from pandas_datareader import data as pdr
import scipy
import yfinance as yf
import numpy as np
import datetime as dt
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from scipy.stats import norm
import csv
import statistics


CSV_file = '/Users/macbookpro/Desktop/python_anaconda/MSPS.CSV'
Date = []
MSPS =[]

with open(CSV_file, 'r') as f:
    reader = csv.DictReader(f)
    for colmn in reader:
        Date.append(colmn.get('DATE'))
        MSPS.append(colmn.get('MSPS'))

#print(tickers)
#print(list_weights)

#weights = np.array(list_weights)
#f_tickers = (np.delete(tickers,42))
#f_weights = (np.delete(weights,42))
#print(MSPS)
#print(f_tickers[0])
New_MSPS = np.array(MSPS)
#np.asarray(MSPS)
#print(np.asarray(New_MSPS) is New_MSPS)
#print(np.std(New_MSPS))

print (type(MSPS))
print (type(New_MSPS))

std = statistics.stdev(MSPS)
print(std)
#plt.title("Home prices")
#ply