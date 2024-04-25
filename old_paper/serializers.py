from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.tokens import RefreshToken
from student_database.utilitys import image_add_db

from .models import Subject, OldPaper

from rest_framework import serializers
from .models import Subject


class Subject_serializer(serializers.ModelSerializer):
    status = serializers.IntegerField(default=200)
    
    class Meta:
        model = Subject
        fields = (
            'id',
            'subject_name',
            'subject_code',
            'branch',
            'year',
            'subject_type',  
            'status',
        )
class OldPaper_serializer(serializers.ModelSerializer):
  status = serializers.IntegerField(default=200)
  class Meta:
    model = OldPaper
    fields = (
        'id',
        'user',
        'file',
        'year',
        'status',

    )

  def create(self, validated_data):
    validated_data.pop('status')
    return OldPaper.objects.create(**validated_data)
