from pandas_datareader import data as pdr
import csv

import yfinance as yf
f = open("myfile.txt", "w")

yf.pdr_override() # <== that's all it takes :-)

# download dataframe using pandas_datareader
data = pdr.get_data_yahoo("SPY", start="2022-01-01", end="2022-01-30")
df.to_csv("C:\Users\hasin\OneDrive\Desktop\Projects\yfinance\CSV.txt")

