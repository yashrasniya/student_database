from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from .serializers import Feedback_serializer
from rest_framework.response import Response
# Create your views here.

class Feedback_view(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        ser=Feedback_serializer(data=request.data)
        if ser.is_valid():
            obj=ser.save(user=request.user)
            return Response(Feedback_serializer(obj).data)
        else:
            return Response({'status':400,'error':ser.errors})