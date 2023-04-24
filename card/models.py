from django.db import models

from list.models import List


class Card(models.Model):
    title = models.CharField(max_length=255, default="")
    description = models.CharField(max_length=255, default="")
    list = models.ForeignKey(List, on_delete=models.CASCADE)
