from rest_framework import generics
from data.models import Restaurant
from .serializers import RestaurantSerializer
from .filters import RestaurantFilter
from django_filters.rest_framework import DjangoFilterBackend

class RestaurantList(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = RestaurantFilter
