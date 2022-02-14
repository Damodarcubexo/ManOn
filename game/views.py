from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from game.models import GameModel
from game.serializers import GameModelSerializer


# class History(APIView):
#     permission_classes = [IsAuthenticated, ]
#     def post(self, request, id):
#         query_set = GameModel.objects.all(id=id)
#         serializer = GameModelSerializer(query_set)
