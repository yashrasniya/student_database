from django.shortcuts import render
from rest_framework import generics
from .models import Event
# Create your views here.

class EevntAPI(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer