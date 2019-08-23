import requests
import numpy as np
import time
from datetime import datetime

# location given here 
location = "Brazil, Ribeirão Preto"
  
# defining a params dict for the parameters to be sent to the API 
PARAMS = {'address':location} 

class Shares():
    '''Class for stock quote searches and analyzing data'''

    def __init__(self, symbol):
        # api-endpoint 
        self.URL = "https://api.worldtradingdata.com/api/v1/history?symbol="+symbol+"&sort=oldest&api_token=DuC3chbLDC5AbPkgtcVo7vkEEW6pkDixHARv3X5oIAltDgo76wq8s9f8V4yc"
    
    def getStockDetails(self, date):

        URL = self.URL+"&date_from="+date+"&date_to="+date

        # sending get request and saving the response as response object 
        r = requests.get(url = URL, params = PARAMS) 
        
        # extracting data in json format 
        data = r.json()

        return data['history'][date]
    
    def getClosing(self, period):
        URL = self.URL+"&date_from="+str(period[0])+"&date_to="+str(period[1])

        # sending get request and saving the response as response object 
        r = requests.get(url = URL, params = PARAMS) 
        
        # extracting data in json format 
        data = r.json()

        closing = [float(data['history'][day]['close']) for day in data['history']]

        return closing
    
    def getVariation(self, period):
        URL = self.URL+"&date_from="+str(period[0])+"&date_to="+str(period[1])

        # sending get request and saving the response as response object 
        r = requests.get(url = URL, params = PARAMS) 
        
        # extracting data in json format 
        data = r.json()

        closing = np.array([[time.mktime(datetime.strptime(day, "%Y-%m-%d").timetuple()),float(data['history'][day]['close'])] for day in data['history']])
        first_day = closing[0,1]
        closing[:,1] = np.around((closing[:,1]/first_day)-1, 3)

        return [closing, first_day]

    def setMarket(self, stock_market):
        self.stock_market = stock_market