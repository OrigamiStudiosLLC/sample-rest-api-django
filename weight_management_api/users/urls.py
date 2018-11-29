from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter

from .views import UserViewSet

routers = DefaultRouter()
routers.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(routers.urls), name='users'),
]
