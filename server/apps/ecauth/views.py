from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.views import APIView
from django.utils.timezone import now
from .authentications import generate_jwt
from .serializers import ECUserSerializer, CaptchaSerializer, ECUserRegisterSerializer
from rest_framework.response import Response
from rest_framework import status
import random
from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.core.mail import send_mail
ECUser = get_user_model()


# Create your views here.
class LoginView(APIView):
    def post(self, request):
        serializer = AuthTokenSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data.get('user')
            user.last_login = now()
            user.save()
            token = generate_jwt(user, 7)
            # have to serializer user instance to get user data and send to frontend
            user_serializer = ECUserSerializer(instance=user)
            return Response({'user': user_serializer.data, 'token': token})
        else:
            return Response({'message': dict(serializer.errors)}, status=status.HTTP_400_BAD_REQUEST)


class CaptchaView(APIView):
    def __init__(self, *args, **kwargs):
        super(CaptchaView, self).__init__(*args, **kwargs)
        self.numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    def generate_captcha(self):
        return ''.join(random.choices(self.numbers, k=4))

    def post(self, request):
        serializer = CaptchaSerializer(data=request.data)

        if serializer.is_valid():
            # generate 4 digits code
            captcha_code = self.generate_captcha()
            # set code to memcache, and expires over 5 mins.
            email = serializer.validated_data.get('email')
            cache.set(email, captcha_code, 60*5)
            print(captcha_code)
            send_mail(
                subject='InnerVue Verification Code',
                message='Your email verification code:' + captcha_code,
                from_email='innervue.sport@gmail.com',
                recipient_list=[email]
            )
            return Response({'message': 'Captcha has been sent, please check your email'},
                            status=status.HTTP_200_OK)
        else:
            return Response({'message': dict(serializer.errors)}, status=status.HTTP_400_BAD_REQUEST)


class ResigterView(APIView):

    def post(self, request):
        serializer = ECUserRegisterSerializer(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')

            user = ECUser.objects.create_user(email=email, username=username, password=password)
            user.last_login = now()
            user.save()

            user_serializer = ECUserSerializer(instance=user)
            token = generate_jwt(user=user, exp_days=7)
            return Response({'user': user_serializer.data, 'token': token})
        else:
            return Response({'message': dict(serializer.errors)}, status=status.HTTP_400_BAD_REQUEST)


# CMS login
class StaffLoginView(APIView):
    def post(self, request):
        serializer = AuthTokenSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data.get('user')
            if user.is_staff == 1:
                user.last_login = now()
                user.save()
                token = generate_jwt(user, 7)
                # have to serializer user instance to get user data and send to frontend
                user_serializer = ECUserSerializer(instance=user)
                return Response({'user': user_serializer.data, 'token': token})
            else:
                return Response({'message': 'You don not have the permission to login management system'},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': dict(serializer.errors)}, status=status.HTTP_400_BAD_REQUEST)