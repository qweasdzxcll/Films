from rest_framework import generics
from .models import User
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .permissions import IsAuthenticatedUser
from rest_framework.authentication import authenticate
from rest_framework import status



class ReadUsersAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class RegisterAPIView(APIView):
    serializer_class= RegisterSerializer
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = Token.objects.create(user = user)
        return Response(
            status=201,
            data={
                "token": token.key
            }
        )

class LoginAPIView(APIView):
    serializer_class= LoginSerializer
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        if username is None or password is None:
            return Response({'error': 'Bad request..'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)

class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        token = get_object_or_404(Token, user=user)
        token.delete()
        return Response()