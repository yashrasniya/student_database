# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router
router = DefaultRouter()

# Register viewsets with the router
router.register(r'images', views.ImageViewSet, basename='image')
router.register(r'subjects', views.SubjectViewSet, basename='subject')
router.register(r'labs', views.LabsViewSet, basename='labs')
router.register(r'departments', views.DepartmentViewSet, basename='department')
router.register(r'navbars', views.NavBarViewSet, basename='navbar')
router.register(r'working-communities', views.WorkingCommunitiesViewSet, basename='working_community')

# Wire up our API using automatic URL routing
# Additionally, include login URLs for the browsable API
urlpatterns = [
    path('', include(router.urls)),
]
