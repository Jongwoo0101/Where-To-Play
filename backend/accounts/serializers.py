from rest_framework import serializers
from .models import *

class UserLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLevel
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    levels = UserLevelSerializer(allow_null=True, required=False)
    class Meta:
        model = CustomUser
        fields = ['username', 'realname', 'nickname', 'email', 'password', 'phonenumber', 'first_priority', 'second_priority', 'third_priority', 'levels']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            realname=validated_data['realname'],
            nickname=validated_data['nickname'],
            email=validated_data['email'],
            phonenumber=validated_data['phonenumber'],
            first_priority=validated_data['first_priority'],
            second_priority=validated_data['second_priority'],
            third_priority=validated_data['third_priority'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user