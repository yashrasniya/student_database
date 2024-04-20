# Import necessary modules
from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Mission, Vision, ActivityImage, Announcement, Course, FooterLink, MenuItem, News, Event, Contact, \
    TopHeaderLink,SliderImage
from .serializers import MissionSerializer, VisionSerializer, ActivityImageSerializer, AnnouncementSerializer, \
    CourseSerializer, FooterLinkSerializer, MenuItemSerializer, NewsSerializer, EventSerializer, ContactSerializer, \
        TopHeaderLinkSerializer,SliderImageSerializer

# Define your views

class MissionAPIView(generics.ListAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

class VisionAPIView(generics.ListAPIView):
    queryset = Vision.objects.all()
    serializer_class = VisionSerializer

class ActivityImageAPIView(generics.ListAPIView):
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
        menu_items = MenuItem.objects.filter(parent=None)
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

class ContactAPIView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class TopHeaderLinkList(generics.ListAPIView):
    queryset = TopHeaderLink.objects.all()
    serializer_class = TopHeaderLinkSerializer

class SliderImageViewSet(viewsets.ModelViewSet):
    queryset = SliderImage.objects.all()
    serializer_class = SliderImageSerializer
