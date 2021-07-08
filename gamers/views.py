from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView

from gamers.serializers import UserRegistrationSerializer


class UserRegistrationAPIView(CreateAPIView):
    """
    This Class Contain User Creation
    """
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        """
        This Method Create New User
        :param request:
        :param *args:
        :param **kwargs:
        :return:
        """
        serializer = self.get_serializer(data=request.data)
        user = serializer.create(validated_data=request.data)

        response = {"id": user.id}

        headers = self.get_success_headers(user)

        return Response(response, status=status.HTTP_201_CREATED, headers=headers)
