# urls.py
from django.urls import path, include
from rest_framework import routers
from .views import MissionAPIView, VisionAPIView, ActivityImageAPIView, AnnouncementViewSet, CourseViewSet, \
    FooterLinkViewSet, MenuAPIView, NewsAPIView, EventAPIView, ContactAPIView, TopHeaderLinkList

app_name = 'home'

router = routers.DefaultRouter()
router.register(r'announcements', AnnouncementViewSet, basename='announcement')
router.register(r'courses', CourseViewSet, basename='course')
router.register(r'footer-links', FooterLinkViewSet, basename='footer-link')

urlpatterns = [
    path('mission/', MissionAPIView.as_view(), name='mission-api'),
    path('vision/', VisionAPIView.as_view(), name='vision-api'),
    path('activity-images/', ActivityImageAPIView.as_view(), name='activity-images-api'),
    path('api/', include(router.urls)),
    path('menu/', MenuAPIView.as_view(), name='menu-api'),
    path('news/', NewsAPIView.as_view(), name='news-api'),
    path('events/', EventAPIView.as_view(), name='events-api'),
    path('contact/', ContactAPIView.as_view(), name='contact-api'),
     path('topheader/', TopHeaderLinkList.as_view(), name='topheader-list'),
]
