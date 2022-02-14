import random
from rest_framework.response import Response
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny, IsAuthenticated
from user_data.permissions import IsOwnerOrReadOnly
from ManOn_backend import settings
from user_data.models import UserTable, Otp
from user_data.serializers import UserTableSerializer, AuthTokenSerializer, SetNewPasswordSerializer, \
    ProfileUpdateSerializer, OtpVerificationSerializer


# Create your views here.
class RegisterAPI(APIView):
    """Api to store the new user details into database"""

    def post(self, request):
        """so save the details and generating the user id"""
        serializer = UserTableSerializer(data=request.data)
        if serializer.is_valid():
            new_key = serializer.save()
            add_value = UserTable.objects.get(id=new_key.pk)
            add_value.user_id = add_value.id + 10000000
            add_value.save()
            return Response({'message': 'successfully registered'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetAPI(APIView):
    """To get the details of every user present in the database"""

    def get(self, request):
        """get the details of users present in database"""
        query_set = UserTable.objects.all()
        serializer = ProfileUpdateSerializer(query_set, many=True)
        return Response({'data': serializer.data})


class LoginAPI(TokenObtainPairView):
    """Api fro user to login into game"""
    permission_classes = (AllowAny,)
    serializer_class = AuthTokenSerializer


class ProfileUpdate(generics.RetrieveUpdateAPIView):
    """Api for Updating the user details and store the updated data"""
    queryset = UserTable.objects.only('id', 'firstName', 'lastName', 'player_name', 'team_name')
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)
    serializer_class = ProfileUpdateSerializer

    def update(self, request, *args, **kwargs):
        """updating the profile and checking the data is valid or not"""
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response({'data': serializer.data}, status=status.HTTP_201_CREATED)


class SentMailView(APIView):
    """Api to sent the otp to user mail  id to reset the password"""

    def post(self, request):
        """sending the otp to user mail id"""
        try:
            user = UserTable.objects.get(email=request.data['email'])
        except UserTable.DoesNotExist:
            return Response({'error': 'Email does not exits.'})
        otp = Otp.objects.create(email=user)

        otp.otp = random.randint(100000, 999999)
        otp.save()
        subject = 'Reset Your Password'
        email_receiver = user.email
        body = f'This is your OTP to reset password {otp.otp}'
        send_mail(subject, body, settings.EMAIL_HOST_USER, [email_receiver, ], fail_silently=False)

        return Response({'success': 'Mail sent'}, status=status.HTTP_200_OK)


# obj1 = SentMailView()
# obj1.


class OtpVerification(APIView):
    serializer_class = OtpVerificationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data,instance=request.data)
        print(request.data)
        # user_object = UserTable.objects.get(email=request.data["email"])
        # print(user_object.pk)
        if serializer.is_valid(raise_exception=True):
            return Response({"otp": "verified"}, status=status.HTTP_200_OK)
        return Response({"otp": "error occured"}, status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordview(generics.UpdateAPIView):
    """Api to reset the password and storing the new password into database"""
    if OtpVerificationSerializer:
        serializer_class = SetNewPasswordSerializer

        def put(self, request, *args, **kwargs):
            """saving the new password of the user into database"""
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            request_email = request.data['email']
            user_object = UserTable.objects.get(email=request_email)
            if UserTable.objects.get(email=request_email):
                user_object.password = make_password(request.data['password'])
                user_object.save()
                return Response({'status': 'password successfully changed'}, status=status.HTTP_201_CREATED)

            return Response({'status': 'An error occured'}, status=status.HTTP_400_BAD_REQUEST)
