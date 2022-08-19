from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from rest_framework.views import APIView

from iheros.user.serializers import (
    UserSerializer,
    UserViewSerializer
)

from iheros.user.models import (
    User
)


class UserViewSet(viewsets.ModelViewSet):

    permission_classes = ()
    authentication_classes = ()

    # serializer_class = None
    # permission_classes_by_action = {
    #     'POST': [permissions.AllowAny], 'PUT': [permissions.IsAuthenticated]}

    # def get_permissions(self):
    #     print("aaaaaaaaaaaaa")
    #     """
    #     Instantiates and returns the list of permissions that this view requires.
    #     """
    #     if self.request.method == 'POST':
    #         permission_classes = [permissions.AllowAny]
    #     else:
    #         permission_classes = [permissions.IsAuthenticated]
    #     return [permission() for permission in permission_classes]

    queryset = User.objects.all()

    # @classmethod
    # def get_extra_actions(cls):
    #     return []

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserSerializer
        return UserViewSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        request.data['password'] = make_password(request.data['password'])
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = serializer.data
        response.pop('password')
        return Response(response, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        change_pass = True if 'password' in request.data else False

        if change_pass:
            request.data['password'] = make_password(request.data['password'])
        else:
            request.data['password'] = instance.password

        serializer = UserSerializer(instance=instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = serializer.data
        response.pop('password')
        return Response(response, status=status.HTTP_200_OK)


class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.queryset.get(id=request.auth["user_id"])
        serializer = self.get_serializer(queryset)
        return Response(serializer.data)
