from django.shortcuts import render
from rest_framework import status
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, get_user_model
# Create your views here.

@api_view(['GET'])
def get_place(request):
    if request.method == 'GET':
        place = PlaceInfo.objects.all()
        serializer = PlaceInfoSerializer(place, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def get_place_detail(request, id):
    if request.method == 'GET':
        place = PlaceInfo.objects.get(id=id)
        serializer = PlaceInfoSerializer(place)
        return Response(serializer.data)

@api_view(['POST']) 
@permission_classes([IsAuthenticated]) # 회원만 장소 추가 가능
def add_place(request):
    if request.method == 'POST':
        try:
            serializer = PlaceInfoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, content_type='multipart/form-data', status=status.HTTP_201_CREATED)
            return Response({'errors': serializer.errors, 'data': request.data}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET', 'POST'])
def write_comment(request):
    if (request.method == 'POST'):
        try:
            serializer = PlaceCommentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    elif (request.method == 'GET'):
        model = PlaceComment.objects.all()
        serializer = PlaceCommentSerializer(model, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def post_image(request):
    if(request.method == 'POST'):
        try:
            serializer = PlaceImageSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, content_type='multipart/form-data', status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    elif (request.method == 'GET'):
        model = PlaceImage.objects.all()
        serializer = PlaceImageSerializer(model, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def write_rating(request, placeinfo_id):
    if (request.method == 'POST'):
        user = get_user_model().objects.get(nickname=request.data.get('user'))
        place = PlaceInfo.objects.get(id=placeinfo_id)
        rating_value = request.data.get('rating')

        try:
            rating = PlaceRating.objects.get(user=user)
            rating.rating = rating_value
            rating.save()
        except PlaceRating.DoesNotExist:
            rating = PlaceRating.objects.create(user=user, rating=rating_value)
            place.ratings.add(rating)
        
        place.save()
        serializer = PlaceRatingSerializer(rating)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    if (request.method == 'GET'):
        ratings = PlaceRating.objects.all()
        serializer = PlaceRatingSerializer(ratings)
        return Response(serializer.data, status=status.HTTP_200_OK)
            
    
@api_view(['GET', 'POST'])
def write_status(request):
    if (request.method == "POST"):
        try:
            serializer = PlaceOpenStatusSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    elif (request.method == "GET"):
        model = PlaceOpenStatus.objects.all()
        serializer = PlaceOpenStatusSerializer(model, many=True)
        return Response(serializer.data)

# @api_view(['GET'])
# def get_placesubinfo(request):
#     model = PlaceSubInfo.objects.all()
#     serializer = PlaceSubInfoSerializer(model, many=True)
#     return Response(serializer.data)