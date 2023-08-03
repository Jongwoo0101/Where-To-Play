from django.shortcuts import render
from rest_framework import status
from .models import PlaceInfo
from .serializers import PlaceInfoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
# Create your views here.

@api_view(['POST']) 
@permission_classes([IsAuthenticated]) # 회원만 장소 추가 가능
def add_place(request):
    if request.method == 'POST':
        try:
            serializer = PlaceInfoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
@api_view(['GET'])
def get_place(request):
    if request.method == 'GET':
        place = PlaceInfo.objects.all()
        serializer = PlaceInfoSerializer(place, many=True)
        return Response(serializer.data)
        