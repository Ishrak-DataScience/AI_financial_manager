from pandas_datareader import data as pdr
import csv

import yfinance as yf

f = open("myfile.txt", "w")

msft = yf.Ticker("MSFT")
Temp=msft.history(period="1y",interval="1d")
writer = csv.writer(f)

# write a row to the csv file
writer.writerow(Temp)
f.close()
