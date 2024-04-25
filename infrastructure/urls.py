# urls.py

from django.urls import path
from .views import InfrastructureListCreate

urlpatterns = [
    path('infrastructures/', InfrastructureListCreate.as_view(), name='infrastructures-list-create'),
]
