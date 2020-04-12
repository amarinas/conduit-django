from rest_framework import serializers

from .models import User

class RegistrationSerializer(serializers.ModelSerializer):

    #Registration and create a new user.

    #password min 8 max is 128
    #characters and not readable why typing
    password =serializers.CharField(
        max_length=128,
        min_length=8,
        write_only= True

    )

    #token is created when registration and token is only read only
    token = serializers.CharField(max+max_length=255, read_only=True)

    class Meta:
        model = User

        fields = ['email', 'username', 'password', 'token']


    def create(self, validated_data):
        #use create_user method to create new user
        return User.objects.create_user(**validated_data)
