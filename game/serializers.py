from rest_framework import serializers
from .models import GameModel, SearchModel


class GameModelSerializer(serializers.Serializer):
    """for serializing data to required format"""
    user_id = serializers.CharField(max_length=20)
    player1 = serializers.CharField(max_length=100)
    player1_score = serializers.IntegerField(default=0)
    player2 = serializers.CharField(max_length=50)
    dateTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M %p")
    player2_score = serializers.IntegerField(default=0)
    player1_team = serializers.CharField(max_length=50)
    player2_team = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return GameModel.objects.create(**validated_data)


class SearchModelSerializer(serializers.ModelSerializer):
    """To serialize and create the data of Searched team"""

    class Meta:
        model = SearchModel
        fields = '__all__'
