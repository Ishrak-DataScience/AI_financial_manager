from pandas_datareader import data as pdr
import csv

import yfinance as yf


class Fetchers:
    def __init__(self, Token_name, start,end):
        self.name = Token_name
        self.start = start
        self.end=end
        self.data = pdr.get_data_yahoo(self.name, start=self.start, end=self.end)
         

        
    def PrintDataFrame(dataframe,path_to_print): 
        Path=path_to_print
        df=dataframe
        df.to_csv(path_or_buf=Path)

    yf.pdr_override() # <== that's all it takes :-)# For making Pandas dataframe

    # download dataframe using pandas_datareader
   
    def GetData(self):
        print(self.data)
        print(type(self.data))
        PrintDataFrame(self.data,'Test2_CSV.csv')
        return self.data

       




