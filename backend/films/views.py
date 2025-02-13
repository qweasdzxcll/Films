from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from rest_framework.permissions import IsAuthenticated


from .models import Film, Review, Actor
from .serializers import FilmSerializer, ReviewSerializer, ActorSerializer
# Create your views here.


class CreateReadFilmsAPIView(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class DetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class ReadCreateReview(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
class ReadCreateActor(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
       
