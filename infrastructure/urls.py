# urls.py

from django.urls import path
from .views import InfrastructureListCreate

urlpatterns = [
    path('api/infrastructures/', InfrastructureListCreate.as_view(), name='infrastructures-list-create'),
]
