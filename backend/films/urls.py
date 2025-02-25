from django.urls import path, include
from rest_framework import routers
from .views import ReadFilmsAPIView, CreateFilmsAPIView, DetailAPIView, ReadCreateReview, ReadCreateActor, SortFilmsAPIView, RatingCreateAPIView, RetrieveUpdateDeleteReview

router = routers.DefaultRouter()

app_name = 'films'

auth_list_patterns = [
    path('', ReadFilmsAPIView.as_view(), name='films'),
    path('create/', CreateFilmsAPIView.as_view(), name='create'),
    path('sort/', SortFilmsAPIView.as_view(), name='sort'),
    path('<int:pk>', DetailAPIView.as_view(), name='film'),
    path('reviews/', ReadCreateReview.as_view(), name='reviews'),
    path('actors/', ReadCreateActor.as_view(), name='actors'),
    path('rating/', RatingCreateAPIView.as_view(), name='rating'),
    path('reviews/<int:pk>', RetrieveUpdateDeleteReview.as_view())
]

urlpatterns = [
    path('', include(auth_list_patterns))
]