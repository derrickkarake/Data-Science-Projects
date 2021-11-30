import pandas as pd
from pandas_datareader import data as pdr
import scipy
import yfinance as yf
import numpy as np
import datetime as dt
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from scipy.stats import norm
    
# Create our portfolio of equities


tickers = ['ACI', 'AAPL' ,'AZO' ,'BRK-B' ,'BA' ,'CHGG' ,'CSCO', 'CCI', 'CVS' ,'DVN' ,'DG',
 'EPD' ,'EQIX' ,'XOM' ,'GS' ,'HA', 'HD' ,'JNJ', 'LDOS' ,'MMP' ,'MARA' ,'MCD' ,'MU',
 'PINS', 'PAA', 'PSA', 'RIOT' ,'RPRX' ,'LUV' ,'SIVB' ,'TDOC' ,'TXT' ,'TMDX', 'UL',
 'U' ,'V', 'WMT' ,'DRIV' ,'SDIV' ,'EEM', 'IDRV']
 
# Set the investment weights (I arbitrarily picked for example)
weights_t = np.array([0.0231, 0.0244, 0.0261, 0.0213, 0.0258, 0.0111, 0.0415, 0.0449 ,0.0371, 0.0145,
 0.0277 ,0.0239 ,0.0203, 0.018 , 0.0279, 0.0315,0.0208, 0.0278 ,0.0232, 0.005,
 0.0073 ,0.0251, 0.0292, 0.0131, 0.0148 ,0.0201, 0.0056,0.0259, 0.0131 ,0.0284,
 0.0161, 0.045 , 0.0204, 0.0174, 0.0127, 0.0101, 0.0343 ,0.0166 ,0.0182 ,0.0201,
 0.0165])

weights = weights_t + 0.0022951219512195122
# Set an initial investment level
initial_investment =144755.27 
 
# Download closing prices
data = yf.download(tickers, start="2011-01-01", end=dt.date.today())['Close']
 
#From the closing prices, calculate periodic returns
returns = data.pct_change()

returns.tail()

#print(returns)

cov_matrix = returns.cov()

print(cov_matrix)
# Calculate mean returns for each stock
avg_rets = returns.mean()
 
# Calculate mean returns for portfolio overall, 
# using dot product to 
# normalize individual means against investment weights
 # https://en.wikipedia.org/wiki/Dot_product#:~:targetText=In%20mathematics%2C%20the%20dot%20product,and%20returns%20a%20single%20number.
port_mean = avg_rets.dot(weights)
 
# Calculate portfolio standard deviation
port_stdev = np.sqrt(weights.T.dot(cov_matrix).dot(weights))
 
# Calculate mean of investment
mean_investment = (1+port_mean) * initial_investment
             
# Calculate standard deviation of investmnet
stdev_investment = initial_investment * port_stdev

# Select our confidence interval (I'll choose 95% here)
conf_level1 = 0.01

# Using SciPy ppf method to generate values for the
# inverse cumulative distribution function to a normal distribution
# Plugging in the mean, standard deviation of our portfolio
# as calculated above
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html
from scipy.stats import norm
cutoff1 = norm.ppf(conf_level1, mean_investment, stdev_investment)

var_1d1 = initial_investment - cutoff1

# Calculate n Day VaR
var_array = []
num_days = int(15)
for x in range(1, num_days+1):    
    var_array.append(np.round(var_1d1 * np.sqrt(x),2))
    print(str(x) + " day VaR @ 99% confidence: " + str(np.round(var_1d1 * np.sqrt(x),2)))

# Build plot
plt.xlabel("Day #")
plt.ylabel("Max portfolio loss (USD)")
plt.title("Max portfolio loss (VaR) over 15-day period")
plt.plot(var_array, "r")
plt.show()
