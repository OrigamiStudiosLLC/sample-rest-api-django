"""
weight_management_api URL Configuration
"""

from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework.authtoken import views

from weight_management_api.users.views import Logout

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('api/(?P<version>(v1|v2))/', include('weight_management_api.users.urls'), name='users'),
    re_path('api/(?P<version>(v1|v2))/', include('weight_management_api.record_weight.urls'), name='user weights'),
    re_path(r'api/(?P<version>(v1|v2))/api_token_auth/', views.obtain_auth_token),
    re_path(r'api/(?P<version>(v1|v2))/logout/', Logout.as_view())
]
