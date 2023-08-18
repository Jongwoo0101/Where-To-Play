from django.shortcuts import render

# Create your views here.
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import *
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated
from .models import *

@api_view(['POST']) # username or email로 로그인
def user_login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        user = None
        if '@' in username:
            try:
                user = CustomUser.objects.get(email=username)
            except ObjectDoesNotExist:
                pass

        if not user:
            user = authenticate(username=username, password=password)
            nickname = CustomUser.objects.filter(username=username).values('nickname')[0]
            level_id = CustomUser.objects.filter(username=username).values('levels')[0]
            level = UserLevelSerializer(UserLevel.objects.get(id=level_id['levels'])).data['level']
        else:
            user = authenticate(username=user, password=password)
            nickname = CustomUser.objects.filter(username=user).values('nickname')[0]
            level_id = CustomUser.objects.filter(username=user).values('levels')[0]
            level = UserLevelSerializer(UserLevel.objects.get(id=level_id['levels'])).data['level']
        
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'nickname': nickname, 'level': level }, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST']) # logout
@permission_classes([IsAuthenticated])
def user_logout(request):
    if request.method == 'POST':
        try:
            request.user.auth_token.delete()
            return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST', 'GET']) # 회원가입
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    else:
        user = CustomUser.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(status=status.HTTP_201_CREATED)
    
@api_view(['POST', 'GET'])
def level(request, nickname):
    user = CustomUser.objects.get(nickname=nickname)
    if request.method == 'POST':
        level = request.data.get('level')
        experience = request.data.get('experience')
        userlevel = UserLevel.objects.create(level=level, experience=experience)
        user.levels.add(userlevel)
        user.save()
        serializer = UserLevelSerializer(userlevel)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'GET':
        model = user.levels.all().values()
        serializer = UserSerializer(model, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

            
