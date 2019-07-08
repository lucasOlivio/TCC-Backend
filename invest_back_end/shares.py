import requests

# location given here 
location = "Brazil, Ribeirão Preto"
  
# defining a params dict for the parameters to be sent to the API 
PARAMS = {'address':location} 

class Shares():
    '''Class for stock quote searches and analyzing data'''

    def __init__(self, symbol):
        # api-endpoint 
        self.URL = "https://api.worldtradingdata.com/api/v1/history?symbol="+symbol+"&sort=newest&api_token=DuC3chbLDC5AbPkgtcVo7vkEEW6pkDixHARv3X5oIAltDgo76wq8s9f8V4yc"
    
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

        closing = [data['history'][day]['close'] for day in data['history']]

        return closing

    def setMarket(self, stock_market):
        self.stock_market = stock_market