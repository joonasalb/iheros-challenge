from rest_framework import serializers

from iheros.threat.models import (
    Threat,
)

from iheros.hero.serializers import (
    HeroSerializer,
)


class ThreatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Threat
        fields = "__all__"


class ThreatsSerializer(serializers.ModelSerializer):
    defeated_by = HeroSerializer(read_only=True)

    class Meta:
        model = Threat
        fields = "__all__"
