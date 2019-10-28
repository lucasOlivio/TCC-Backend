import requests
import numpy as np
import time
from datetime import datetime, timedelta
import re

# location given here 
location = "Brazil, Ribeirão Preto"
  
# defining a params dict for the parameters to be sent to the API 
PARAMS = {'address':location} 

class Shares():
    '''Class for stock quote searches and analyzing data'''

    SECTORS = ['Energy','Basic Materials','Industrials','Consumer Cyclical','Consumer Defensive',
           'Healthcare','Financial Services','Technology',
           'Communication Services','Utilities','Real Estate']

    def __init__(self, symbol, url = 0):
        self.url = url
        self.symbol = symbol
        # api-endpoint 
        self.URLs = ["https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol="+symbol+"&apikey=LFXEILQ0E30J3BZO","https://api.worldtradingdata.com/api/v1/history?symbol="+symbol+"&sort=oldest&api_token=DuC3chbLDC5AbPkgtcVo7vkEEW6pkDixHARv3X5oIAltDgo76wq8s9f8V4yc"]
    
    def getStockDetails(self, date):

        URL = self.URLs[self.url]+("&date_from="+date+"&date_to="+date if self.url==0 else "")

        # sending get request and saving the response as response object 
        r = requests.get(url = URL, params = PARAMS) 
        
        # extracting data in json format 
        data = r.json()

        # normalizing dict keys
        if self.url==0:
            send = { re.sub('^[0-9]. +','',key) : val for key, val in data['Time Series (Daily)']['-'.join(reversed(date.split('/')))].items()}
        else:
            try:
                send = data['history']['-'.join(reversed(date.split('/')))]
            except Exception as e:
                print(e)
                send = False
        return send
    
    def getClosing(self, period):
        URL = self.URLs[self.url]+"&date_from="+str(period[0])+"&date_to="+str(period[1])

        # sending get request and saving the response as response object 
        r = requests.get(url = URL, params = PARAMS) 
        
        # extracting data in json format 
        data = r.json()

        try:
            closing = [float(data['history'][day]['close']) for day in data['history']]
        except Exception as e:
            closing = False

        return closing
    
    def getVariation(self, period):
        URL = self.URLs[self.url]+"&date_from="+str(period[0])+"&date_to="+str(period[1])

        # sending get request and saving the response as response object 
        r = requests.get(url = URL, params = PARAMS) 
        
        # extracting data in json format 
        data = r.json()

        try:
            closing = np.array([[time.mktime(datetime.strptime(day, "%Y-%m-%d").timetuple()),float(data['history'][day]['close'])] for day in data['history']])
            first_day = closing[0,1]
            closing[:,1] = np.around((closing[:,1]/first_day)-1, 3)
            resp = [closing, first_day]
        except Exception as e:
            resp = False

        return resp