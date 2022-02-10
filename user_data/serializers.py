from django.contrib.auth import password_validation
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from user_data.models import UserTable


class UserTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTable
        # fields = '__all__'
        fields = ['email', 'password', 'firstName', 'lastName', 'player_name', 'user_id', 'team_name']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserTableSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        instance.firstName = validated_data.get('firstName', instance.firstName)
        instance.lastName = validated_data.get('lastName', instance.lastName)
        instance.player_name = validated_data.get('player_name', instance.player_name)
        instance.team_name = validated_data.get('team_name', instance.team_name)
        instance.save()
        return instance


class AuthTokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        return token


# class ProfileUpdateSerializer(serializers.Serializer):
#     class Meta:
#         model = UserTable
#         fields = ['firstName', 'lastName', 'player_name', 'team_name']
#
#     def update(self, instance, validated_data):
#         instance.firstName = validated_data.get('firstName', instance.firstName)
#         instance.lastName = validated_data.get('lastName', instance.lastName)
#         instance.player_name = validated_data.get('player_name', instance.player_name)
#         instance.team_name = validated_data.get('team_name', instance.team_name)
#         instance.save()
#         return instance
