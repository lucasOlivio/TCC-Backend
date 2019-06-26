from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from invest_back_end.shares import Shares
from pandas.tseries.offsets import BDay
import datetime

from invest_back_end.models import Profile

class MainGraphView(APIView):
    '''Simple class to return the data of the stock'''
    permission_classes = (IsAuthenticated,)

    # Receives the request and returns the json with the message
    def get(self, request):

        if request.GET.get('symbol')!='':
            today = datetime.datetime.now()
            week_ago = (today - BDay(7)).date()
            month_ago = (today - datetime.timedelta(days=31)).date()
            year_ago = (today - datetime.timedelta(days=365)).date()

            share = Shares(request.GET['symbol'])

            stockClose_week = share.getClosing([week_ago, today])
            stockClose_month = share.getClosing([month_ago, today])
            stockClose_year = share.getClosing([year_ago, today])

            resp = True
            data = [
                stockClose_week,
                stockClose_month,
                stockClose_year,
            ]
            content = {
                'resp': resp,
                'data':data
            }
        else:
            content = {
                'resp': 'Nenhuma ação informada!'
            }

        return Response(content)

class MainDataView(APIView):
    '''Simple class to return the data of the user'''
    permission_classes = (IsAuthenticated,)

    # Receives the request and returns the json with the message
    def get(self, request):

        content = {
                'resp': request.META
            }

        return Response(content)