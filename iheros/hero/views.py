from iheros.hero.serializers import (
    HeroSerializer,
)
from iheros.hero.models import (
    Hero,
)
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from iheros.api import common as common
from rest_framework import status
from pathlib import Path
import environ
import os

BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))


# Create your views here.


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.save()
        response = {
            "success": True,
            "message": "Herói atualizado com sucesso!"
        }
        return Response(response, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):

        instance = self.get_object()

        try:
            instance.delete()
            response = {
                "success": True,
                "message": "Herói removido com sucesso!"
            }
            status_response = status.HTTP_204_NO_CONTENT
        except:
            response = {
                "success": False,
                "message": "Erro ao escluir herói, tente novamente!"
            }
            status_response = status.HTTP_403_FORBIDDEN

        return Response(response, status=status_response)
