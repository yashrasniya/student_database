# urls.py
from django.urls import path
from .views import MissionAPIView, VisionAPIView, ActivityImageAPIView, AnnouncementViewSet, CourseViewSet, \
    FooterLinkViewSet, MenuAPIView, NewsAPIView, EventAPIView, ContactAPIView, TopHeaderLinkList,SliderImageViewSet

app_name = 'home'

urlpatterns = [
    path('mission/', MissionAPIView.as_view(), name='mission-api'),
    path('vision/', VisionAPIView.as_view(), name='vision-api'),
    path('activity-images/', ActivityImageAPIView.as_view(), name='activity-images-api'),
    path('announcements/', AnnouncementViewSet.as_view({'get': 'list'}), name='announcement-list'),
    path('announcements/<int:pk>/', AnnouncementViewSet.as_view({'get': 'retrieve'}), name='announcement-detail'),
    path('courses/', CourseViewSet.as_view({'get': 'list'}), name='course-list'),
    path('courses/<int:pk>/', CourseViewSet.as_view({'get': 'retrieve'}), name='course-detail'),
    path('footer-links/', FooterLinkViewSet.as_view({'get': 'list'}), name='footer-link-list'),
    path('footer-links/<int:pk>/', FooterLinkViewSet.as_view({'get': 'retrieve'}), name='footer-link-detail'),
    path('menu/', MenuAPIView.as_view(), name='menu-api'),
    path('news/', NewsAPIView.as_view(), name='news-api'),
    path('events/', EventAPIView.as_view(), name='events-api'),
    path('contact/', ContactAPIView.as_view(), name='contact-api'),
    path('topheader/', TopHeaderLinkList.as_view(), name='topheader-list'),
    path('slider-images/', SliderImageViewSet.as_view({'get': 'list'}), name='slider-images-list'),
]

