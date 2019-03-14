from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class HelloView(APIView):
    '''Simple class to return a hello message'''
    permission_classes = (IsAuthenticated,)

    # Receives the request and returns the json with the message
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)