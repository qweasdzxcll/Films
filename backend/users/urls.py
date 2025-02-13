from django.urls import path, include
from .views import RegisterAPIView, LoginAPIView, LogoutAPIView, ReadUsersAPIView


app_name = 'users'

urls_list = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('', ReadUsersAPIView.as_view(), name='read')
]


urlpatterns = [
    path('', include(urls_list))
]