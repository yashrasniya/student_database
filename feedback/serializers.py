from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.tokens import RefreshToken
from student_database.utilitys import image_add_db

from .models import Feedback



class Feedback_serializer(serializers.ModelSerializer):
  status=serializers.IntegerField(default=200)
  class Meta:
    model = Feedback
    fields = (
      'id',
      'user',
      'subject',
      'message',
      'status',

    )

  def create(self, validated_data):
    validated_data.pop('status')
    return Feedback.objects.create(**validated_data)




