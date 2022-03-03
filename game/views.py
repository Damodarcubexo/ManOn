import datetime
import operator
import re
from functools import reduce

from django.db.models import Q
from rest_framework import status

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from game.models import GameModel, SearchModel
from game.serializers import GameModelSerializer, SearchModelSerializer
from user_data.models import UserTable
from user_data.permissions import IsOwnerOrReadOnly


class GameView(APIView):
    """ Api for post the game history and retrive the game history"""
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

    def get(self, request):
        """to get the game history and will shown to user"""
        query_set = GameModel.objects.filter(user_id=request.user.id)
        serializer = GameModelSerializer(query_set, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        """To store the the game details"""
        user = UserTable.objects.get(id=request.user.id)
        opponent = UserTable.objects.get(user_id=request.data['user_id'])
        # datetime.datetime
        if opponent.player_name != user.player_name:

            data = {
                "user_id": user.id,
                'player1': user.player_name,
                "player1_team": user.team_name,
                "player2": opponent.player_name,
                "dateTime": datetime.datetime.now(),
                "player2_team": opponent.team_name,
                "player1_score": request.data['player1_score'],
                "player2_score": request.data['player2_score'],
            }
            serializer = GameModelSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "user can't play with himself"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        # print()
        snippet = GameModel.objects.get(id=request.query_params["id"])
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SearchPlayer(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        query = []
        result = re.match("[a-z0-9]+@[a-z]+\.[a-z]{2,3}", request.query_params["id"])
        query.append(Q(email=request.query_params['id'])) if result else query.append(
            Q(user_id=request.query_params['id']))
        if UserTable.objects.filter(reduce(operator.or_, query)).exists():
            User = UserTable.objects.get(reduce(operator.or_, query))
            if request.user == User:
                return Response({"details": "You can't play with your self"}, status=status.HTTP_404_NOT_FOUND)
            print(User.email)
            data = {
                "user": request.user.id,
                "player_id": User.user_id,
                "player_name": User.player_name,
                "player_team": User.team_name,
                "email": User.email
            }
            player = SearchModel.objects.filter(user=request.user.id)
            if player.filter(player_id=User.user_id).exists():
                pass
            else:
                serializer = SearchModelSerializer(data=data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()

            return Response({
                "user_id": User.user_id,
                "player_name": User.player_name,
                "player_team": User.team_name,
                "email": User.email,
            }, status=status.HTTP_200_OK)

        return Response({"details": "We can't find any account "}, status=status.HTTP_404_NOT_FOUND)


class SearchHistory(APIView):
    """To get the details of every user present in the database"""
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)

    def get(self, request):
        """get the details of users search history"""
        query_set = SearchModel.objects.filter(user=request.user.id)
        serializer = SearchModelSerializer(query_set, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
