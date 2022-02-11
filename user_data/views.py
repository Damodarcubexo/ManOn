from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import IsOwnerOrReadOnly
import random
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from ManOn_backend import settings
from .models import UserTable, Otp
from .serializers import UserTableSerializer, AuthTokenSerializer, SetNewPasswordSerializer
from rest_framework import status, generics


# Create your views here.
class RegisterAPI(APIView):
    def post(self, request):
        print("hii")
        serializer = UserTableSerializer(data=request.data)
        UserTable.objects.all().first()
        if serializer.is_valid():
            new_key = serializer.save()
            add_value = UserTable.objects.get(id=new_key.pk)
            add_value.user_id = add_value.id + 10000000
            add_value.save()
            return Response(UserTableSerializer(add_value).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPI(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = AuthTokenSerializer


class ProfileUpdate(generics.RetrieveUpdateAPIView):
    queryset = UserTable.objects.all()
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)
    serializer_class = UserTableSerializer

class SentMailView(APIView):
    def post(self, request):
        try:
            user = UserTable.objects.get(email=request.data['email'])
        except UserTable.DoesNotExist:
            return Response({'error': 'Email does not exits.'})
        otp = Otp.objects.create(email=user)

        otp.otp = random.randint(100000, 999999)
        otp.save()
        subject = 'Reset Your Password'
        to = user.email
        body = f'This is your OTP to reset password {otp.otp}'
        send_mail(subject, body, settings.EMAIL_HOST_USER, [to, ], fail_silently=False)

        return Response({'success': 'Mail sent'}, status=status.HTTP_200_OK)


class ResetPasswordview(generics.UpdateAPIView):
    serializer_class = SetNewPasswordSerializer

    def put(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        request_email = request.data['email']
        user_object = UserTable.objects.get(email=request_email)
        if UserTable.objects.get(email=request_email):
            user_object.password = make_password(request.data['password'])
            user_object.save()
            # Otp.objects.filter(email=serializer.validated_data.get('otp')).delete()
            return Response({'status': 'password successfully changed'}, status=status.HTTP_201_CREATED)

        return Response({'status': 'An error occured'}, status=status.HTTP_400_BAD_REQUEST)
