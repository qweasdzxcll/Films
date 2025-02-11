from django.urls import path, include
from .views import RegisterAPIView


app_name = 'users'

urls_list = [
    path('register/', RegisterAPIView.as_view(), name='register')
]


urlpatterns = [
    path('', include(urls_list))
]