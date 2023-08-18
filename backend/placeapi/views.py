from django.shortcuts import render
from rest_framework import status, viewsets
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
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

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def adjust_place_detail(request, placeinfo_id):
    serializers = PlaceInfoSerializer(data=request.data)
    try:
        if serializers.is_valid():
            place = PlaceInfo.objects.get(id=placeinfo_id)
            if (request.data.get('image') != None):
                place.image = request.data.get('image')
            place.name = request.data.get('name')
            place.lat = request.data.get('lat')
            place.lng = request.data.get('lng')
            place.address = request.data.get('address')
            place.contact = request.data.get('contact')
            place.homepage = request.data.get('homepage')
            place.time = request.data.get('time')
            place.description = request.data.get('description')
            place.save()
            return Response(status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def comment(request, placeinfo_id):
    if (request.method == 'POST'):
        try:
            user = get_user_model().objects.get(nickname=request.data.get('username'))
            place = PlaceInfo.objects.get(id=placeinfo_id)
            comment_value = request.data.get('comment')

            comment = PlaceComment.objects.create(username=user, comment=comment_value)
            place.comments.add(comment)
            place.save()
            serializer = PlaceCommentSerializer(comment)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(e)

    elif (request.method == 'GET'):
        model = PlaceInfo.comments.all()
        serializer = PlaceCommentSerializer(model)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def image(request, placeinfo_id):
    if (request.method == 'POST'):
        try:
            user = get_user_model().objects.get(nickname=request.data.get('username'))
            place = PlaceInfo.objects.get(id=placeinfo_id)
            image_data = request.data.get('image')
            if (image_data != None):
                image = PlaceImage.objects.create(username=user, image=image_data)
                place.sub_images.add(image)
                place.save()
                serializer = PlaceImageSerializer(image)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(e)

    elif (request.method == 'GET'):
        model = PlaceInfo.sub_images.all()
        serializer = PlaceCommentSerializer(model)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def rating(request, placeinfo_id):
    if (request.method == 'POST'):
        user = get_user_model().objects.get(nickname=request.data.get('user'))
        place = PlaceInfo.objects.get(id=placeinfo_id)
        rating_value = request.data.get('rating')

        try: # rating은 1명이 1개만 쓸 수 있기에 평점 존재 시 수정 처리
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
@permission_classes([IsAuthenticatedOrReadOnly])
def placestatus(request, placeinfo_id):
    place = PlaceInfo.objects.get(id=placeinfo_id)
    
    if (request.method == "POST"):
        user = get_user_model().objects.get(nickname=request.data.get('username'))
        openstatus = request.data.get('open_status')
        open_status = PlaceOpenStatus.objects.create(username=user, open_status=openstatus)
        place.open_statuses.add(open_status)
        place.save()
        serializer = PlaceOpenStatusSerializer(open_status)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    elif (request.method == "GET"):
        model = place.open_statuses.all().last()
        serializer = PlaceOpenStatusSerializer(model)
        return Response(serializer.data)
    
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

# @api_view(['GET'])
# def get_placesubinfo(request):
#     model = PlaceSubInfo.objects.all()
#     serializer = PlaceSubInfoSerializer(model, many=True)
#     return Response(serializer.data)