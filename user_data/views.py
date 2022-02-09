from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import UserTable
from .serializers import UserTableSerializer, AuthTokenSerializer
from rest_framework import status


# Create your views here.
class RegisterAPI(APIView):
    def post(self, request):
        print("hii")
        serializer = UserTableSerializer(data=request.data)
        # print(serializer)
        UserTable.objects.all().first()
        if serializer.is_valid():
            new_key = serializer.save()
            add_value = UserTable.objects.get(id=new_key.pk)
            add_value.user_id = add_value.id + 10000
            add_value.save()
            return Response(UserTableSerializer(add_value).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPI(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = AuthTokenSerializer
