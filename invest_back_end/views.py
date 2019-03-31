from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from invest_back_end.shares import Shares


class MainGraphView(APIView):
    '''Simple class to return the data of the user'''
    permission_classes = (IsAuthenticated,)

    # Receives the request and returns the json with the message
    def get(self, request):
        today = datetime.datetime.now()
        week_ago = (today - BDay(7)).date()
        month_ago = (today - BDay(31)).date()
        year_ago = (today - BDay(365)).date()

        share = Shares('AAPL')

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
        return Response(content)