from rest_framework import serializers
from .models import *


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class PracticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Practical
        fields = '__all__'


class LabSerializer(serializers.ModelSerializer):
    practical = PracticeSerializer(many=True)

    class Meta:
        model = Lab
        fields = '__all__'



class DepartmentSerializer(serializers.ModelSerializer):
    department_labs_name=LabSerializer(many=True)
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



