from rest_auth.registration.serializers import RegisterSerializer
from .models import User
from rest_auth.serializers import LoginSerializer
from rest_framework import serializers


class CustomRegisterSerializer(RegisterSerializer):
    username = None
    name = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('name')

    # def save(self, request):
    #     return user


class CustomLoginSerializer(LoginSerializer):
    username = None

    class Meta:
        model = User
        fields = ('name', 'password')


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('avatar', 'about')

    def validate(self, data):

        about = data.get('about', None)
        avatar = data.get('avatar', None)

        if about == '':
            about = None
        if avatar is None and about is None:
            raise ValueError('that is not correct eh')
        return data
