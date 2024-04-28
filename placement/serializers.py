from rest_framework import serializers
from .models import PlacementCell, Recruiter, Achievement, Cell, Head, Subtitle

class SubtitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtitle
        fields = '__all__'

class HeadSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Head
        fields = '__all__'

class CellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cell
        fields = '__all__'

class PlacementCellSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlacementCell
        fields = '__all__'

class RecruiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruiter
        fields = '__all__'

class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = '__all__'
