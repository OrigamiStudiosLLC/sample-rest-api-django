from django.urls import path

from .views import UserWeightView

urlpatterns = [
     path('weights/', UserWeightView.as_view(), name="users-all")
]
