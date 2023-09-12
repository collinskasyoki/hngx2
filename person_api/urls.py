"""
URL configuration for person_api project.
"""
from django.urls import path

from .views import PersonViewSet

urlpatterns = [
    path('api/', PersonViewSet.as_view(), name='person-list'),
    path('api/<int:user_id>/', PersonViewSet.as_view(), name='person-detail')
]