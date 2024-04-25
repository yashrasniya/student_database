from django.urls import path
from . import views

app_name= 'department'

urlpatterns = [
    path('departments/', views.DepartmentViewSet.as_view(), name='department-list'),
    path('images/', views.ImageViewSet.as_view(), name='image-list'),
    path('labs/', views.LabsViewSet.as_view(), name='labs-list'),
    path('working-communities/', views.WorkingCommunitiesViewSet.as_view(), name='working-communities-list'),
    path('navbar/', views.NavBarViewSet.as_view(), name='navbar-list'),
    # Add more URL patterns for other views as needed
]
