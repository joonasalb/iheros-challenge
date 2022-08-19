from django.db import models
from django.utils.translation import ugettext_lazy as _
from iheros.api import common as common
from iheros.hero.models import Hero


class Threat(models.Model):

    monster_name = models.CharField(
        max_length=100, verbose_name='Monster name')
    danger_level = models.CharField(
        verbose_name='DangerLevel', max_length=30, choices=common.DangerLevel.choices, default=common.DangerLevel.Wolf)
    defeated_by = models.ForeignKey(Hero, verbose_name='defeated_by', null=True,
                                    blank=True, on_delete=models.CASCADE, related_name="threats")
    location = models.JSONField(
        verbose_name='Location coordinates', null=False)
    updated_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Updated at")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Created at")

    class Meta:
        verbose_name = 'Threat'
        verbose_name_plural = 'Threats'
