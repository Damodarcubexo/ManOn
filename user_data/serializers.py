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


class AuthTokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        return token
