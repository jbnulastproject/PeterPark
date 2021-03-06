from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","username","email")
class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username','password','email')
        extra_kwargs = {"password": {"write_only": True}}
        
        def create(self,validated_data):
            users = User.objects.create_user(validated_data["username"], validated_data["password"],validated_data["email"])
            return users


class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()  
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Unable to log in with provided credentials.")
