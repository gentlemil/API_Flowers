from rest_framework import serializers
from .models import Category, Room, Plant

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'url',
            'name',
            'slug',
            
        ]

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = [
            'id',
            'url',
            'name',
            'temperature',
            'expose',
            'humidity',
            'draft',
        ]

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = [
            'id',
            'url',
            'name',
            'category',
            'room',
            'watering_interval',
            'fertilizing_interval',
            'required_exposure',
            'required_temperature',
            'required_humidity',
            'blooming',
            'difficulty',
            'last_watered',
            'last_fertilized',
        ]


