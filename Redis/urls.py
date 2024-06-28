from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from Redis.views import *

router = routers.DefaultRouter()

#API
router.register(r'musician', MusicianViewSet, basename='musician')
router.register(r'album', AlbumViewSet, basename='album')

urlpatterns = [
    path("redis/", include(router.urls), name='MusicApi'),
    ]