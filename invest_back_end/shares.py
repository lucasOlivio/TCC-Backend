from iexfinance.stocks import Stock
from datetime import datetime
from iexfinance.stocks import get_historical_data

class Shares():
    '''Class for stock quote searches and analyzing data'''

    def __init__(self, symbol):
        #stock_market: in wich market will be the search ("IBOV",)
        self.symbol = symbol
    
    def getStock(self, period):

        dt_start = [ int(x) for x in period[0].split('/') ]
        
        dt_end = [ int(x) for x in period[1].split('/') ]

        start = datetime(dt_start[2], dt_start[0], dt_start[1]).strftime('%Y-%m-%d')

        end = datetime(dt_end[2], dt_end[0], dt_end[1]).strftime('%Y-%m-%d')

        df = get_historical_data(self.symbol,start, end, output_format='json', token="sk_8010a6c7ada647499af72f12ec9da15e")

        return end
    
    def getClosing(self, period):
        start = period[0]

        end = period[1]

        df = get_historical_data(self.symbol,start, end, output_format='pandas', token="sk_8010a6c7ada647499af72f12ec9da15e")

        return df['close']

    def setMarket(self, stock_market):
        self.stock_market = stock_market