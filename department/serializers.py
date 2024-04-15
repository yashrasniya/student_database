from rest_framework import serializers
from .models import *

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

'''class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
'''
class LabsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Labs
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class NavBarSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavBar
        fields = '__all__'

class WorkingCommunitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Working_communities
        fields = '__all__'
