# views.py
from rest_framework import generics
from .models import *
from .serializers import ImageSerializer,  LabsSerializer, DepartmentSerializer, NavBarSerializer, WorkingCommunitiesSerializer

class ImageViewSet(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

'''class SubjectViewSet(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
'''
class LabsViewSet(generics.ListAPIView):
    queryset = Labs.objects.all()
    serializer_class = LabsSerializer

class DepartmentViewSet(generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class NavBarViewSet(generics.ListAPIView):
    queryset = NavBar.objects.all()
    serializer_class = NavBarSerializer

class WorkingCommunitiesViewSet(generics.ListAPIView):
    queryset = Working_communities.objects.all()
    serializer_class = WorkingCommunitiesSerializer
