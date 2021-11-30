import numpy as np
from pandas_datareader.yahoo.daily import YahooDailyReader 
import yfinance as yf
import pandas as pd
from pandas_datareader import data as pdr
import datetime as dt

weights = np.array([0.0231, 0.0244, 0.0261, 0.0213, 0.0258, 0.0111, 0.0415, 0.0449 ,0.0371, 0.0145,
 0.0277 ,0.0239 ,0.0203, 0.018 , 0.0279, 0.0315,0.0208, 0.0278 ,0.0232, 0.005,
 0.0073 ,0.0251, 0.0292, 0.0131, 0.0148 ,0.0201, 0.0056,0.0259, 0.0131 ,0.0284,
 0.0161, 0.045 , 0.0204, 0.0174, 0.0127, 0.0101, 0.0343 ,0.0166 ,0.0182 ,0.0201,
 0.0165]).astype(np.float64)

print(len(weights))

print(0.0941/41)

k = 0.0022951219512195122 

b = weights + k 

print(b)
print (k + weights[1])