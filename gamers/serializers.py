from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from gamers.models import GameUser
from arena.general_helper.general_messages import EXIST_USER, PASSWORD_MISMATCH, USER_CREATION_ERROR


class UserSerializer(serializers.ModelSerializer):
    """
    This Class Performs Serialization For New Gamer User Registration.
    """
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "username", "email", "password", "confirm_password")

    def validate(self, attrs):
        """
        This Method Check Exist Of The New Game User And Validate Password and Confirm Password.
        :param attrs:
        :return:
        """
        try:
            username_exist = User.objects.filter(
                username=attrs.get("username"),
                is_active=True
            ).exists()

            if username_exist:
                error = {"message": EXIST_USER}

                raise serializers.ValidationError(error)

            if attrs.get('password') != attrs.get('confirm_password'):
                error = {"message": PASSWORD_MISMATCH}

                raise serializers.ValidationError(error)
        except Exception:
            error = {"message": USER_CREATION_ERROR}

            raise serializers.ValidationError(error)
        finally:
            del attrs['confirm_password']
            attrs['password'] = make_password(attrs['password'])

            return attrs


class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    This Class Performs User And Gamer User Model Serialize And Create New Game User
    """
    user = UserSerializer(required=True)
    birthdate = serializers.CharField(write_only=True)
    about = serializers.CharField(write_only=True)

    class Meta:
        model = GameUser
        fields = ("user", "birthdate", "about")

    def create(self, validated_data):
        """
        This Function Override The Default Create Method Of The Model Serializer.
        :param validated_data: Data Contains All The Details Of User
        :return: Returns A Successfully Created User Record
        """
        user_serializer = UserSerializer(data=validated_data["user"])
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()

        super(UserRegistrationSerializer, self).create({
            "user": user,
            "birthdate": validated_data["birthdate"],
            "about": validated_data["about"]
        })

        return user


class UserSearchSerializer(serializers.Serializer):
    """
    This Class Search Gamer User Details
    """
    key = serializers.CharField(required=True)
    value = serializers.CharField(required=True)

    def __init__(self, *args, **kwargs):
        super(UserSearchSerializer, self).__init__(*args, **kwargs)

        self.search_keys = {
            "username": "user__username",
            "first_name": "user__first_name",
            "last_name": "user__last_name",
            "birthdate": GameUser.birthdate
        }
        self.user = None

    def validate(self, attrs):
        """
        This Function Validates User Authenticate And Return User Details
        :param attrs:
        :return:
        """
        attrs = dict(attrs)

        if attrs.get('key') not in self.search_keys.keys():
            raise serializers.ValidationError("User Search Keyword Invalid")

        return attrs

    def get_user(self, validated_data):
        """
        This Method Return Gamer Details By Search Key
        :param validated_data:
        :return:
        """
        key = validated_data["key"]

        users = GameUser.objects.filter(
            self.search_keys[key] == validated_data["value"]
        )

        return list(users)
