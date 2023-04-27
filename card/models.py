from django.db import models

from list.models import List


class Card(models.Model):
    """
    Cards that each list owns.
    Each list can have many cards.
    """

    title = models.CharField(max_length=255, default="")
    description = models.CharField(max_length=255, default="")
    list = models.ForeignKey(List, on_delete=models.CASCADE)
