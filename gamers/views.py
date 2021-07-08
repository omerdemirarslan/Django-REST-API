from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.authentication import BasicAuthentication

from gamers.models import GameUser

from gamers.serializers import UserRegistrationSerializer, UserSearchSerializer


class UserRegistrationAPIView(CreateAPIView):
    """
    This Class Contain User Creation
    """
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        """
        This Method Create New Game User
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        serializer = self.get_serializer(data=request.data)
        user = serializer.create(validated_data=request.data)

        response = {"id": user.id}

        headers = self.get_success_headers(user)

        return Response(response, status=status.HTTP_201_CREATED, headers=headers)


class UsersProfileAPIView(GenericAPIView):
    """
    This Class Return Authenticated User's Data After Basic Authentication
    """
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        This Method Returns Authenticated Game User's Information
        :param request:
        :return:
        """
        user_details = GameUser.objects.get(user=request.user.id)

        return Response(
            data={
                "about": user_details.about,
                "birthdate": user_details.birthdate,
                "date_joined": user_details.user.date_joined,
                "first_name": user_details.user.first_name,
                "last_name": user_details.user.last_name,
            },
            status=status.HTTP_200_OK,
        )


class UserSearchAPIView(GenericAPIView):
    """
    This Class Filters The Database With Different Key Names
    """
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = UserSearchSerializer

    def __init__(self, *args, **kwargs):
        self.request_data = None
        self.seralizer = None

    def get_queryset(self):
        """
        This Function Create Query Set For Database Filter
        :return:
        """
        users = GameUser.objects.filter(
            **{
                self.serializer.search_keys[self.request_data["key"]]: self.request_data["value"],
                "user__is_active": True
            }
        ).select_related()

        return [
            {
                "id": user.user.id,
                "user_name": user.user.username,
                "first_name": user.user.first_name,
                "last_name": user.user.last_name,
                "about": user.about,
                "birthdate": user.birthdate
            }
            for user in users
        ]

    def get(self, request):
        """
        This Function Returns Database Search Result
        :return:
        """
        data = dict(request.GET)

        self.request_data = {
            "key": list(data.keys())[0],
            "value": list(data.values())[0][0]
        }

        self.serializer = self.get_serializer(data=self.request_data)
        self.serializer.is_valid(raise_exception=True)

        return Response(
            data=self.get_queryset(),
            status=status.HTTP_200_OK,
        )
