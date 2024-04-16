from django.urls import path, include  # Import the include function
from .views import BookListCreate, BookRetrieveUpdateDestroy, StaffListCreate, StaffRetrieveUpdateDestroy, AnnouncementListCreate, AnnouncementRetrieveUpdateDestroy

app_name = 'library'

urlpatterns = [
    path('books/', BookListCreate.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroy.as_view(), name='book-retrieve-update-destroy'),
    path('staff/', StaffListCreate.as_view(), name='staff-list-create'),
    path('staff/<int:pk>/', StaffRetrieveUpdateDestroy.as_view(), name='staff-retrieve-update-destroy'),
    path('announcements/', AnnouncementListCreate.as_view(), name='announcement-list-create'),
    path('announcements/<int:pk>/', AnnouncementRetrieveUpdateDestroy.as_view(), name='announcement-retrieve-update-destroy'),
    ]
