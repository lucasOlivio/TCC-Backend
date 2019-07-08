from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework.authtoken.models import Token

from invest_back_end.shares import Shares
from pandas.tseries.offsets import BDay
import datetime
import json

from django.contrib.auth.models import User
from invest_back_end.models import Profile, update_profile, GraphComp, save_graphcomp, del_graphcomp, StockDetail, save_stockdetail, del_stockdetail
from django.core import serializers

class MainStockDataView(APIView):
    '''Simple class to return the data of the stock'''
    permission_classes = (IsAuthenticated,)

    # Receives the request and returns the json with the message
    def post(self, request):

        content = {
                'resp': 'ok'
            }
        
        if request.POST['method'] == 'mainGraph':
            if request.POST.get('symbol')!='':
                today = datetime.datetime.now()
                week_ago = (today - BDay(7)).date()
                month_ago = (today - datetime.timedelta(days=31)).date()
                year_ago = (today - datetime.timedelta(days=365)).date()

                share = Shares(request.POST['symbol'])

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
        elif request.POST['method'] == 'compGraph':
            if request.POST.get('symbol')!='':
                today = datetime.datetime.now()
                one_year = (today - datetime.timedelta(days=365)).date()
                two_year = (today - datetime.timedelta(days=730)).date()
                three_year = (today - datetime.timedelta(days=1095)).date()

                share = Shares(request.POST['symbol'].split(','))

                stockClose_1year = share.getClosing([one_year, today])
                stockClose_2year = share.getClosing([two_year, today])
                stockClose_3year = share.getClosing([three_year, today])

                resp = True
                data = [
                    stockClose_1year,
                    stockClose_2year,
                    stockClose_3year,
                ]
                content = {
                    'resp': resp,
                    'data':data
                }
            else:
                content = {
                    'resp': 'Nenhuma ação informada!'
                }
        else:
            return Response({'resp':'No method '+request.POST['method']})

        return Response(content)

class MainDataView(APIView):
    '''Simple class to return the data of the user'''
    permission_classes = (IsAuthenticated,)

    # Receives the request and returns the json with the message
    def post(self, request):

        token = request.META['HTTP_AUTHORIZATION'].replace('Token ','')

        if request.POST['method'] == 'load':

            content = User.objects.filter(auth_token__key=token).values('username','first_name')[0]
            content.update(Profile.objects.filter(user__auth_token__key=token).values('gender','age')[0])

            return Response(content)
        
        elif request.POST['method'] == 'save':
            update_profile(
                token,
                request.POST['username'],
                request.POST['first_name'],
                request.POST['gender'],
                request.POST['age'],
            )

            return Response({'resp':True})
        else:
            return Response({'resp':'No method '+request.POST['method']})

class CompGraphView(APIView):
    '''Class to manage the list of the users graph comparations'''
    permission_classes = (IsAuthenticated,)

    # Receives the request and returns the json with the message
    def post(self, request):

        token = request.META['HTTP_AUTHORIZATION'].replace('Token ','')

        if request.POST['method'] == 'load':

            content = GraphComp.objects.filter(user__auth_token__key=token, ).values('index', 'stock','description','color').order_by('index')

            content_dict = { i : content[i] for i in range(0, len(content) ) }

            return Response(content_dict)
        
        elif request.POST['method'] == 'save':
            save_graphcomp(
                token, 
                request.POST['index'], 
                request.POST['stock'], 
                request.POST['description'],
                request.POST['color'],
            )

            return Response({'resp':1})
        elif request.POST['method'] == 'del':
            del_graphcomp(
                token, 
                request.POST['index'],
                request.POST['stock'],
            )

            return Response({'resp':1})
        else:
            return Response({'resp':'No method '+request.POST['method']})

class StockDetailView(APIView):
    '''Class to manage the list of the users stock details'''
    permission_classes = (IsAuthenticated,)

    # Receives the request and returns the json with the message
    def post(self, request):

        token = request.META['HTTP_AUTHORIZATION'].replace('Token ','')

        if request.POST['method'] == 'load':

            content = StockDetail.objects.filter(user__auth_token__key=token, ).values('stock','description').order_by('stock')

            content_dict = { i : content[i] for i in range(0, len(content) ) }

            return Response(content_dict)
        
        elif request.POST['method'] == 'save':
            save_stockdetail(
                token, 
                request.POST['stock'], 
                request.POST['description'],
            )

            return Response({'resp':1})
        elif request.POST['method'] == 'del':
            del_stockdetail(
                token, 
                request.POST['stock'],
            )

            return Response({'resp':1})
        
        elif request.POST['method'] == 'details':
            share = Shares(request.POST['symbol'])

            stockDetail = share.getStock([request.POST['date'], request.POST['date']])

            return Response(stockDetail)
        else:
            return Response({'resp':'No method '+request.POST['method']})