from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('categories', views.CategoryViewSet)
router.register('rooms', views.RoomViewSet)
router.register('plants', views.PlantViewSet)

urlpatterns = [
    path('', include(router.urls))
]