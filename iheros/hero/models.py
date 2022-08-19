from django.db import models
from django.utils.translation import ugettext_lazy as _
from iheros.api import common as common


class Hero(models.Model):

    name = models.CharField(max_length=100, verbose_name='Name')
    rank = models.CharField(verbose_name='Rank', max_length=20,
                            choices=common.Rank.choices, default=common.Rank.S)
    latitude = models.FloatField(verbose_name='Latitude')
    longitude = models.FloatField(verbose_name='Longitude')

    launch_time = models.DateTimeField(
        auto_now_add=True, verbose_name="Launch time")
    updated_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Updated at")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Created at")

    class Meta:
        verbose_name = 'Hero'
        verbose_name_plural = 'Heros'
        ordering = ['created_at']
