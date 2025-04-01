import pandas as pd
import matplotlib.pyplot as plt
from alpha_vantage.cryptocurrencies import CryptoCurrencies
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.econindicators import EconIndicators
from alpha_vantage.options import Options
from alpha_vantage.alphaintelligence import AlphaIntelligence
from alpha_vantage.commodities import Commodities
from alpha_vantage.foreignexchange import ForeignExchange
from alpha_vantage.fundamentaldata import FundamentalData
import json

class AlphaVantageAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.cryptocurrencies = CryptoCurrencies(key=self.api_key)
        self.techindicators = TechIndicators(key=self.api_key,output_format='pandas')
        self.timeseries = TimeSeries(key=self.api_key)
        self.econindicators = EconIndicators(key=self.api_key)
        self.options = Options(key=self.api_key)
        self.alphaintelligence = AlphaIntelligence(key=self.api_key)
        self.commodities = Commodities(key=self.api_key)
        self.foreignexchange = ForeignExchange(key=self.api_key)
        self.fundamentaldata = FundamentalData(key=self.api_key)

    def call_method(self, client_name, method_name, *args, **kwargs):
      
        clients = {
            'cryptocurrencies': self.cryptocurrencies,
            'techindicators': self.techindicators,
            'timeseries': self.timeseries,
            'econindicators': self.econindicators,
            'options': self.options,
            'alphaintelligence': self.alphaintelligence,
            'commodities': self.commodities,
            'foreignexchange': self.foreignexchange,
            'fundamentaldata': self.fundamentaldata,
        }
        client = getattr(client_name,method)
        
        client = clients.get(client_name)
        if client is None:
            raise ValueError(f"Client {client_name} does not exist.")
        
       
        method = getattr(client, method_name, None)
        if method is None:
            raise ValueError(f"Method {method_name} does not exist in {client_name}.")
        
        
        return method(*args, **kwargs)

    
if __name__ == "__main__":
    api = AlphaVantageAPI(api_key='1712GHWMXRW4HY3P')
    df = api.call_method('timeseries', 'get_intraday', 'IBM', '5min')
    print(df)
    

