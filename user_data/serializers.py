
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
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


class ProfileUpdateSerializer(serializers.Serializer):
    firstName = serializers.CharField(max_length=150)
    lastName = serializers.CharField(max_length=150)
    player_name = serializers.CharField(max_length=150)
    team_name = serializers.CharField(max_length=150)

    def update(self, instance, validated_data):
        instance.firstName = validated_data.get('firstName', instance.firstName)
        instance.lastName = validated_data.get('lastName', instance.lastName)
        instance.player_name = validated_data.get('player_name', instance.player_name)
        instance.team_name = validated_data.get('team_name', instance.team_name)
        instance.save()
        return instance



