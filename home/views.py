from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from .serializers import OldPaper_serializer, Subject_serializer
from rest_framework.response import Response

from .models import Banner

# views.py
from rest_framework import generics
from .models import Mission, Vision, ActivityImage, Announcement, Course, FooterLink
from .serializers import MissionSerializer, VisionSerializer, ActivityImageSerializer, AnnouncementSerializer, CourseSerializer, FooterLinkSerializer
from rest_framework import viewsets

class MissionAPIView(generics.ListCreateAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

class VisionAPIView(generics.ListCreateAPIView):
    queryset = Vision.objects.all()
    serializer_class = VisionSerializer

class ActivityImageAPIView(generics.ListCreateAPIView):
    queryset = ActivityImage.objects.all()
    serializer_class = ActivityImageSerializer

class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class FooterLinkViewSet(viewsets.ModelViewSet):
    queryset = FooterLink.objects.all()
    serializer_class = FooterLinkSerializer
