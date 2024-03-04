from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.tokens import RefreshToken
from student_database.utilitys import image_add_db



# serializers.py
from .models import Mission, Vision, ActivityImage, Announcement, Course, FooterLink

class MissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = '__all__'

class VisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vision
        fields = '__all__'

class ActivityImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityImage
        fields = '__all__'


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__' 

class FooterLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterLink
        fields = '__all__'
