from datetime import datetime
from datetime import timedelta
from iheros.threat.serializers import (
    ThreatSerializer,
    ThreatsSerializer
)
from iheros.threat.models import (
    Threat,
)
from iheros.hero.models import (
    Hero,
)
from rest_framework import viewsets, permissions
from rest_framework.response import Response
import environ
from pathlib import Path
import os
from iheros.api import common as common
from ..hero import helpers as helpers
from django.http import JsonResponse
from django.forms.models import model_to_dict


BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))


# Create your views here.

class ThreatViewSet(viewsets.ModelViewSet):
    queryset = Threat.objects.all()
    serializer_class = ThreatSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ThreatSerializer
        return ThreatsSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class AssignmentThreatViewSet(viewsets.ModelViewSet):
    queryset = Threat.objects.all()
    serializer_class = ThreatSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, **kwargs):

        danger_level = request.data["danger_level"]
        monster_name = request.data["monster_name"]
        latitude = request.data["location"]["latitude"]
        longitude = request.data["location"]["longitude"]
        location = latitude, longitude
        current_time = datetime.now()
        rank = common.ranked_options[danger_level]

        try:
            query = 'SELECT *, (6371 \
                            * acos(cos(radians(-30.053831)) \
                            * cos(radians(%s)) \
                            * cos(radians(%s) - radians(-51.191810)) \
                            + sin(radians(-30.053831)) \
                            * sin(radians(%s)) )) AS distance \
                            FROM public.hero_hero \
                            WHERE rank = %s AND launch_time < %s \
                            ORDER BY distance ASC \
                            LIMIT 1'
            heroes = Hero.objects.raw(
                query, [latitude, longitude, latitude, rank, current_time])  # latitude, longitude, latitude, rank, current_time

            closest_hero = None
            if len(heroes) > 0:
                closest_hero = helpers.searchClosestHero(heroes, location)
            else:

                heroes = Hero.objects.raw(
                    query, [latitude, longitude, latitude, rank, current_time])  # latitude, longitude, latitude, rank, current_time

                if len(heroes) > 0:
                    closest_hero = helpers.searchClosestHero(heroes, location)
                else:
                    new_threat = {
                        "danger_level": danger_level,
                        "monster_name": monster_name,
                        "location": {
                            "latitude": latitude,
                            "longitude": longitude
                        },
                        "defeated_by": None,
                    }
                    serializer_threat = ThreatSerializer(data=new_threat)

                    serializer_threat.is_valid(raise_exception=True)
                    serializer_threat.save()
                    resp = {
                        "success": True,
                        "message": "Nenhum Herói disponivel para a batalha =/",
                    }
                    return Response(resp)

            future_time = current_time + \
                timedelta(minutes=float(
                    common.recovery_time_grid[danger_level]))

            if closest_hero is not None:
                hero_closest = Hero.objects.get(id=closest_hero.id)
                hero_closest.launch_time = future_time
                hero_closest.save()

            new_threat = {
                "danger_level": danger_level,
                "monster_name": monster_name,
                "location": {
                    "latitude": latitude,
                    "longitude": longitude
                },
                "defeated_by": hero_closest.id,
            }
            serializer_threat = ThreatSerializer(data=new_threat)

            serializer_threat.is_valid(raise_exception=True)
            serializer_threat.save()

            resp = {
                "success": True,
                "closest_hero": model_to_dict(hero_closest),
            }
            return JsonResponse(resp)

        except Exception:
            resp = {
                "sucess": False,
                "mesage": "Erro ao atribuir o Herói ao Ataque",
            }
            return Response(resp)
