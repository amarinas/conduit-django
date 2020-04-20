from rest_framework import serializers
from django.contrib.auth import authenticate

from conduit.apps.profiles.serializers import ProfileSerializer
from .models import User

class RegistrationSerializer(serializers.ModelSerializer):

    #Registration and create a new user.

    #password min 8 max is 128
    #characters and not readable why typing
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only= True

    )

    #token is created when registration and token is only read only
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User

        fields = ['email', 'username', 'password', 'token']


    def create(self, validated_data):
        #use create_user method to create new user
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):

        email = data.get('email', None)
        password = data.get('password', None)

        #exception if not vaild
        if email is None:
            raise serializers.ValidationError(
                'Email is needed to Login'
            )

        if password is None:
            raise serializers.ValidationError(
                'Password is needed to Login'
            )

        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError(
                'user is not found please try again'
            )

        if not user.is_active:
            raise serializers.ValidationError(
                'user has been deactivated'
            )

        return {
            'email': user.email,
            'username': user.username,
            'token': user.token
        }

class UserSerializer(serializers.ModelSerializer):
    # handles serialization and deserialization of user objects

    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
        )
    profile = ProfileSerializer(write_only=True)
    bio = serializers.CharField(source='profile.bio', read_only=True)
    image = serializers.CharField(source="profile.image", read_only=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'token', 'profile', 'bio', 'image',)

        read_only_fields = ('token',)

    def update(self, instance, validated_data):
        # update user
        password = validated_data.pop('password', None)
        profile_data = validated_data.pop('profile', {})

        for (key, value) in validated_data.items():
            seattr(instance, key, value)

        if password is not None:

            instance.set_password(password)

        instance.save()

        for (key, value) in profile_data.items():
            setattr(instance.profile, key, value)

        instance.profile.save()

        return instance
