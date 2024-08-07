from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .serializers import LoginSerializer, UserInfoSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import login



class LoginAPIView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data["user"]
            
            # Log the user in
            login(request, user)

            # Generate and return a token
            token, created = Token.objects.get_or_create(user=user)

            # Serialize user information
            info_serializer = UserInfoSerializer(user)

            return Response(
                {'token': token.key, 'user_info': info_serializer.data}, 
                status=status.HTTP_200_OK
            )


class LogoutAPIView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        token = request.auth

        # Now, you can delete the token
        token.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
    
class SinUpAPIView(APIView):
    
    authentication_classes = []
    permission_classes = [AllowAny]
    
    pass