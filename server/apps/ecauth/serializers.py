from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model
from django.core.cache import cache
ECUser = get_user_model()


class ECUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ECUser
        exclude = ['password']


class CaptchaSerializer(serializers.Serializer):
    email = serializers.EmailField(validators=
                                   [UniqueValidator(queryset=ECUser.objects.all(),
                                                    message='This user already exists, please log in instead')],
                                   error_messages={'messages': 'Please enter a valid email address'})


class ECUserRegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(validators=[UniqueValidator(queryset=ECUser.objects.all(),
                                                               message='This user already exists')])
    username = serializers.CharField(min_length=2, max_length=100)
    captcha = serializers.CharField(min_length=4, max_length=4)
    password = serializers.CharField(min_length=8)
    confirmPassword = serializers.CharField(min_length=8)

    def validate(self, data):
        email = data.get('email')
        cached_captcha = cache.get(email)
        print(cached_captcha)
        if data.get('password') != data.get('confirmPassword'):
            raise serializers.ValidationError('Passwords does not match')
        if data.get('captcha') != cached_captcha:
            raise serializers.ValidationError('Verification code is not correct')
        return data


