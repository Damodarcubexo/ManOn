from rest_framework import serializers
from .models import GameModel


class GameModelSerializer(serializers.Serializer):
    """for serializing data to required format"""
    user_id = serializers.CharField(max_length=20)
    player1 = serializers.CharField(max_length=100)
    player1_score = serializers.IntegerField(default=0)
    player2 = serializers.CharField(max_length=50)
    player2_score = serializers.IntegerField(default=0)
    player1_team = serializers.CharField(max_length=50)
    player2_team = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return GameModel.objects.create(**validated_data)

