from rest_framework import serializers
from .models import GameModel


class GameModelSerializer(serializers.Serializer):
    game_id = serializers.IntegerField(read_only=True)
    player1 = serializers.StringRelatedField(many=True)
    player1_score = serializers.IntegerField(default=0)
    player2 = serializers.CharField(max_length=50)
    player2_score = serializers.IntegerField(default=0)
    datetime = serializers.DateTimeField()
    player1_team = serializers.CharField(max_length=50)
    player2_team = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return GameModel.objects.create(**validated_data)
