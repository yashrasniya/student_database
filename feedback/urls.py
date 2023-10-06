from django.urls import path
from .views import Feedback_view
urlpatterns = [
    path('feedback/', Feedback_view.as_view()),

]