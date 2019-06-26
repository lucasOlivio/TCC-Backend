from iexfinance.stocks import Stock
from datetime import datetime
from iexfinance.stocks import get_historical_data

class Shares():
    '''Class for stock quote searches and analyzing data'''

    def __init__(self, symbol):
        #stock_market: in wich market will be the search ("IBOV",)
        self.symbol = symbol
    
    def getStock(self, period):
        start = period[0]

        end = period[1]

        df = get_historical_data(self.symbol,start, end, output_format='json')

        return df
    
    def getClosing(self, period):
        start = period[0]

        end = period[1]

        df = get_historical_data(self.symbol,start, end, output_format='pandas')

        return df['close']

    def setMarket(self, stock_market):
        self.stock_market = stock_market