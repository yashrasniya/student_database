# views.py

from rest_framework import generics
from .models import Infrastructure
from .serializers import InfrastructureSerializer

class InfrastructureListCreate(generics.ListAPIView):
    queryset = Infrastructure.objects.all()
    serializer_class = InfrastructureSerializer
