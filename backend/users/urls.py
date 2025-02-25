from django.urls import path, include
from .views import RegisterUserAPIView, LoginUserAPIView, LogoutUserAPIView


app_name = 'users'

urls_list = [
    path('', RegisterUserAPIView.as_view(), name='register'),
    path('login/', LoginUserAPIView.as_view(), name='login'),
    path('logout/', LogoutUserAPIView.as_view(), name='logout'),
]


urlpatterns = [
    path('', include(urls_list))    
]