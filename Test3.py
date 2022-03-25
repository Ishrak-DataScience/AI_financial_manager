from pandas_datareader import data as pdr
import csv

import yfinance as yf
f = open("myfile.txt", "w")

#Definations

def PrintDataFrame(dataframe,path_to_print): 
    Path=path_to_print
    df=dataframe
    df.to_csv(path_or_buf=Path)

yf.pdr_override() # <== that's all it takes :-)

# download dataframe using pandas_datareader
data = pdr.get_data_yahoo("SPY", start="2022-01-01", end="2022-01-30")
print(data)
print(type(data))
PrintDataFrame(data,'Test2_CSV.csv')



