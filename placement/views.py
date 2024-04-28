from rest_framework import generics
from .models import PlacementCell, Recruiter, Achievement, Cell, Head, Subtitle
from .serializers import PlacementCellSerializer, RecruiterSerializer, AchievementSerializer, CellSerializer, HeadSerializer, SubtitleSerializer

class SubtitleList(generics.ListAPIView):
    queryset = Subtitle.objects.all()
    serializer_class = SubtitleSerializer

class HeadList(generics.ListAPIView):  
    queryset = Head.objects.all()
    serializer_class = HeadSerializer

class PlacementCellListAPIView(generics.ListAPIView):
    queryset = PlacementCell.objects.all()
    serializer_class = PlacementCellSerializer

class RecruiterListAPIView(generics.ListAPIView):
    queryset = Recruiter.objects.all()
    serializer_class = RecruiterSerializer

class AchievementListCreate(generics.ListAPIView):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer

class AchievementRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer

class CellListCreate(generics.ListAPIView):
    queryset = PlacementCell.objects.all()
    serializer_class = PlacementCellSerializer

class CellRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cell.objects.all()
    serializer_class = CellSerializer
