from rest_framework import generics, views, status
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.decorators import api_view
from django.db.models import Avg

from users.permissions import IsAdmin, IsOwnerOrReadOnly


from .models import Film, Review, Actor, Rating
from .serializers import FilmSerializer, ReviewSerializer, ActorSerializer, RatingSerializer
# Create your views here.


class CreateFilmsAPIView(generics.CreateAPIView):
    # permission_classes = [IsAdmin]
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class ReadFilmsAPIView(generics.ListAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = FilmSerializer

    def get_queryset(self):
        queryset = Film.objects.all()
        search_value = self.request.GET.get('title')
        filter_value = self.request.GET.get('genre')
        if filter_value:
            queryset = queryset.filter(genre=filter_value)
        if search_value:
            queryset = queryset.filter(title__icontains=search_value)
        return queryset

class SortFilmsAPIView(generics.ListAPIView):
    serializer_class = FilmSerializer

    def get_queryset(self):
        return Film.objects.annotate(avg_rating=Avg('rating__rating')).order_by('-avg_rating')

class DetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAdmin]
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class ReadCreateReview(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class RetrieveUpdateDeleteReview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_permissions(self):
        if self.request.method in ['GET', 'POST']:
            return [IsOwnerOrReadOnly()]
            
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        return Response({'message': response.data})
    
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return Response(response.data, status=status.HTTP_200_OK)
    
    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        return Response(response.data, status=status.HTTP_204_NO_CONTENT)
    
    def put(sef, request, *args, **kwargs):
        response = super().put(request, *args, **kwargs)
        return Response(response.data)
    
class ReadCreateActor(generics.ListCreateAPIView):
    # permission_classes = [IsAdmin]
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
       
class RatingCreateAPIView(views.APIView):
    serializer_class = RatingSerializer
    def post(self, request):
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            rating = serializer.save()
            rating.film.update_average_rating()
            return Response(serializer.data)