# views.py
from rest_framework import generics
from .models import Mission, Vision, ActivityImage, Announcement, Course, FooterLink, MenuItem, News, Event, Contact,TopHeaderLink
from .serializers import MissionSerializer, VisionSerializer, ActivityImageSerializer, AnnouncementSerializer, \
    CourseSerializer, FooterLinkSerializer, MenuItemSerializer, NewsSerializer, EventSerializer, ContactSerializer, \
        TopHeaderLinkSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

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

class MenuAPIView(APIView):
    def get(self, request, format=None):
        menu_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)
        return Response(serializer.data)

class NewsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        news_data = News.objects.all()
        serializer = NewsSerializer(news_data, many=True)
        return Response(serializer.data)

class EventAPIView(APIView):
    def get(self, request, *args, **kwargs):
        event_data = Event.objects.all()
        serializer = EventSerializer(event_data, many=True)
        return Response(serializer.data)



class ContactAPIView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    

class TopHeaderLinkList(generics.ListCreateAPIView):
    queryset = TopHeaderLink.objects.all()
    serializer_class = TopHeaderLinkSerializer
    