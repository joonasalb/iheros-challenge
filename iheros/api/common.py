from django.db import models
from django.utils.translation import ugettext_lazy as _


class Rank(models.TextChoices):
    S = 'S', _('S')
    A = 'A', _('A')
    B = 'B', _('B')
    C = 'C', _('C')


class DangerLevel(models.TextChoices):
    God = 'God', _('God')
    Dragon = 'Dragon', _('Dragon')
    Tiger = 'Tiger', _('Tiger')
    Wolf = 'Wolf', _('Wolf')


ranked_options = {
    'God': "S",
    'Dragon': "A",
    'Tiger': "B",
    'Wolf': "C",
}

recovery_time_grid = {
    'God': 60 * 10,  # 10 minutes
    'Dragon': 60 * 5,  # 5 minutes
    'Tiger': 20,  # 20 seconds
    'Wolf': 2,  # 2 seconds
}
