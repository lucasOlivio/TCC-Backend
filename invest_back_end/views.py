from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class MainGraphView(APIView):
    '''Simple class to return the data of the user'''
    permission_classes = (IsAuthenticated,)

    # Receives the request and returns the json with the message
    def get(self, request):
        resp = True
        data = [
            [1,2,3,4,5,6,7,8,9,10],
            [2,1,5,6,4,9,7,0,5,3],
            [4,4,6,8,9,9,2,10,10,10],
        ]
        content = {
            'resp': resp,
            'data':data
        }
        return Response(content)