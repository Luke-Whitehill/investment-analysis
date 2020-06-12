import matplotlib.pyplot as plot
from scipy.stats import norm
import math
import scipy.stats as stats
from scipy import stats
import matplotlib.pyplot as plt
import yfinance as yf
import numpy as np

stocks = ['EOS.AX']
data = yf.download(tickers="EOS.AX",
                   start="2017-01-01", group_by="ticker", interval="1d")  # ['Adj Close']


close = data['Adj Close']
plt.subplot(2, 1, 1)
plt.plot(close)
plt.ylabel('Stock price in $')
print(close)
plt.subplot(2, 1, 2)
rets1 = np.log(close / close.shift(1))
rets1 = rets1[2:len(rets1)]
rets = data['Adj Close'].pct_change()
rets = rets[~np.isnan(rets)]
plt.plot(rets)


# Fit a normal distribution to the data:
mu, std = norm.fit(rets)

# Plot the histogram.

plt.figure(2)
plt.hist(rets, bins=100, density=True, alpha=0.6, color='b')

# Plot the PDF.
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)
plt.plot(x, p, 'k', linewidth=2)
title = "Fit results: mu = %.2f,  std = %.2f" % (mu, std)
plt.title(title)

plt.show()

""" plt.figure(4)
# The variable 'rets1' will be our histogram plotting variable.

# Fit a normal distribution to the data:
mu, std = norm.fit(rets1)
# Plot histogram
plt.hist(rets1, bins, density=True)
# Plotting the PDF
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu)
plt.plot(x, p, 'k', linewidth=2)
title = "Fit results: mu = %.2f, std = %.2f" % (mu, std)
plt.title(title)
plt.show() """


data_market = yf.download(tickers="^AORD",
                          start="2015-01-01", group_by="ticker", interval="1d")  # ['Adj Close']
marketret = data_market['Adj Close'].pct_change()
marketret = marketret[~np.isnan(marketret)]
print(marketret)


""" plt.figure(4)
plt.scatter(marketret, rets)
plt.show()
corr = stats.pearsonr(marketret, rets)
print(corr[0]) """
