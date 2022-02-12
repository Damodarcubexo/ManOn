from rest_framework import serializers, status
from .models import GameModel


class GameModelSerializer(serializers.Serializer):
    player1 = serializers.CharField(max_length=100)
    player1_score = serializers.IntegerField(default=0)
    player2 = serializers.CharField(max_length=50)
    player2_score = serializers.IntegerField(default=0)
    # datetime = serializers.DateTimeField()
    player1_team = serializers.CharField(max_length=50)
    player2_team = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return GameModel.objects.create(**validated_data)