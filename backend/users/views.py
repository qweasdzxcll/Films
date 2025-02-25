from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from .authentication import Bearer


from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework import status



class RegisterUserAPIView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class LoginUserAPIView(APIView):
    serializer_class = UserSerializer
    def post(self, request, *args, **kwargs):
        phone = request.data.GET.get('phone')
        if phone:
            user = User.objects.get(phone=phone)
        token, _ = Bearer.objects.get_or_create(user=user)
        return Response({'token': token.key})

class LogoutUserAPIView(APIView):
    def get(self, request, *args, **kwargs):
        token = Bearer.objects.get(user=request.user)
        token.delete()
        return Response({'message': 'token was deleted'})
    