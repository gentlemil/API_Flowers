from django.shortcuts import render

from rest_framework import viewsets
from .models import Category, Room, Plant
from .serializers import CategorySerializer, RoomSerializer, PlantSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = CategorySerializer
class PlantViewSet(viewsets.ModelViewSet):
    queryset = Plant.objects.all()
    serializer_class = CategorySerializer


# Create your views here.
