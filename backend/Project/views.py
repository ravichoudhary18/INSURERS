from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ServerTest(APIView):

    def get(self, requests):
        return Response({'server': 'runing'}, status=status.HTTP_200_OK)