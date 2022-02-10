import random

from django.contrib.auth import password_validation
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from user_data.models import UserTable, Otp


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


# class ResetPasswordSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Otp
#         fields = '__all__'
#
#     def validate(self, attrs):
#         if attrs['email'] != attrs['email']:
#             otp = random.randint(100000, 999999)
#             attrs['otp'] = otp
#         return attrs
    #
    # def update(self, instance, validated_data):
    #     instance.set_password(validated_data['new_password'])
    #     instance.save()
    #     return instance


class SetNewPasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, max_length=20)
    otp = serializers.CharField(min_length=6, max_length=6)
    email = serializers.EmailField(min_length=1, max_length=30)

    class Meta:
        model = Otp
        fields = '__all__'

    def validate_otp(self, otp):
        if otp:
            if Otp.objects.filter(otp=otp):
                return otp
            return serializers.ValidationError('OTP does not matched')
        return serializers.ValidationError('OTP does not exits.')
