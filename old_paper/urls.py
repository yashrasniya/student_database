from django.urls import path
from .views import Subject_view,OldPaper_view
urlpatterns = [
    path('subject/', Subject_view.as_view()),
    path('OldPaper/<int:id>/', OldPaper_view.as_view()),

]