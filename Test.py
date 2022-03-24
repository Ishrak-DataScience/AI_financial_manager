from pandas_datareader import data as pdr

import yfinance as yf
yf.pdr_override() # <== that's all it takes :-)

# download dataframe
data = pdr.get_data_yahoo("SPY", start="2017-01-01", end="2017-04-30")
print("printing SPY")
print(data)

msft = yf.Ticker("MSFT")

print("printing microsoft info")
# get stock info
print(msft.info)

# get historical market data
print("printing microsoft history")
hist = msft.history(period="max")

print(hist)

tickers = yf.Tickers('aapl goog')
# ^ returns a named tuple of Ticker objects

# access each ticker using (example)




