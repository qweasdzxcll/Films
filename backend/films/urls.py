from django.urls import path, include
from rest_framework import routers
from .views import CreateReadFilmsAPIView, DetailAPIView, ReadCreateReview

router = routers.DefaultRouter()

app_name = 'films'

auth_list_patterns = [
    path('', CreateReadFilmsAPIView.as_view(), name='films'),
    path('<int:pk>', DetailAPIView.as_view(), name='film'),
    path('reviews/', ReadCreateReview.as_view(), name='reviews')
]

urlpatterns = [
    path('', include(auth_list_patterns))
]