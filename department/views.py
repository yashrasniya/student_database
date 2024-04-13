# views.py
from rest_framework import generics
from .models import *
from .serializers import ImageSerializer, SubjectSerializer, LabsSerializer, DepartmentSerializer, NavBarSerializer, WorkingCommunitiesSerializer

class ImageViewSet(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class SubjectViewSet(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class LabsViewSet(generics.ListCreateAPIView):
    queryset = Labs.objects.all()
    serializer_class = LabsSerializer

class DepartmentViewSet(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class NavBarViewSet(generics.ListCreateAPIView):
    queryset = NavBar.objects.all()
    serializer_class = NavBarSerializer

class WorkingCommunitiesViewSet(generics.ListCreateAPIView):
    queryset = Working_communities.objects.all()
    serializer_class = WorkingCommunitiesSerializer
