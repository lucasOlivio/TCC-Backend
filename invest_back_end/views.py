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
            [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0],
            [2.0,1.0,5.0,6.0,4.0,9.0,7.0,0.0,5.0,3.0],
            [4.0,4.0,6.0,8.0,9.0,9.0,2.0,10.0,10.0,10.0],
        ]
        content = {
            'resp': resp,
            'data':data
        }
        return Response(content)