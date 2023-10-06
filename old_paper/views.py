from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from .serializers import OldPaper_serializer, Subject_serializer
from rest_framework.response import Response
from .models import Subject, OldPaper


# Create your views here.

class Subject_view(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        branch = request.GET.get('branch', '')
        year = request.GET.get('year', '')
        if not (branch and year):
            return Response({'error': 'branch or year not provided'}, )
        obj = Subject.objects.filter(branch=branch, year=year)
        print(Subject.objects.all().values())
        return Response(Subject_serializer(obj, many=True, context={'request': request}).data)


class OldPaper_view(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        obj = OldPaper.objects.filter(subject=id)
        return Response(OldPaper_serializer(obj, many=True, context={'request': request}).data)
