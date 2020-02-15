from django.contrib import admin
from .models import Category, Room, Plant

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug',]
    
class RoomAdmin(admin.ModelAdmin):
    list_display = ['name', 'temperature', 'expose', 'humidity', 'draft']

class PlantAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'room', 'watering_interval', 'fertilizing_interval', 'required_exposure', 'required_temperature', 'required_humidity', 'blooming', 'difficulty', 'last_watered', 'last_fertilized']
    list_filter = ['name', 'category', 'room']
    search_fields = ['name', 'category', 'room']
    ordering = ['name', 'category', 'room']
    # autocomplete_fields = ['category', 'room']
    
    
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Plant, PlantAdmin)