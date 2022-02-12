from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from game.models import GameModel
from game.serializers import GameModelSerializer
from user_data.models import UserTable
from user_data.permissions import IsOwnerOrReadOnly


class GameView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, id):
        print(id)
        print(request.data)
        user = UserTable.objects.get(id=id)
        print(user.id)
        opponent = UserTable.objects.get(user_id=request.data['user_id'])
        data = {

                'player1': user.team_name,
                "player1_team": user.player_name,
                "player2": opponent.player_name,
                "player2_team": opponent.team_name,
                "player1_score": request.data['player1_score'],
                "player2_score": request.data['player2_score'],
                }
        serializer = GameModelSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            print(serializer)
            print('hiii')
            serializer.save()
            return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
