from django.urls import path
from . import views

urlpatterns = [
    path('heads/', views.HeadList.as_view(), name='head-list'),  
    path('cells/', views.CellListCreate.as_view(), name='cell-list'),
    path('cells/<int:pk>/', views.CellRetrieveUpdateDestroy.as_view(), name='cell-detail'),
    path('achievements/', views.AchievementListCreate.as_view(), name='achievement-list'),
    path('achievements/<int:pk>/', views.AchievementRetrieveUpdateDestroy.as_view(), name='achievement-detail'),
    path('placement-cells/', views.PlacementCellListAPIView.as_view(), name='placement-cell-list'),
    path('recruiters/', views.RecruiterListAPIView.as_view(), name='recruiter-list'),
    path('subtitles/', views.SubtitleList.as_view(), name='subtitle-list'),
]
