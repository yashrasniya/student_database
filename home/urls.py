#urls.py
from django.urls import path, include
from rest_framework import routers
from .views import MissionAPIView, VisionAPIView, ActivityImageAPIView, AnnouncementViewSet, CourseViewSet, FooterLinkViewSet


router = routers.DefaultRouter()
router.register(r'announcements', AnnouncementViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'footer-links', FooterLinkViewSet)

urlpatterns = [
    path('mission/', MissionAPIView.as_view(), name='mission-api'),
    path('vision/', VisionAPIView.as_view(), name='vision-api'),
    path('activity-images/', ActivityImageAPIView.as_view(), name='activity-images-api'),
    path('api/', include(router.urls)),
    path('api/', include(router.urls)),
    path('api/', include(router.urls)),
    # Add other URLs as needed
]

