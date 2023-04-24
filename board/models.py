from django.db import models

from workspace.models import Workspace


class Board(models.Model):
    name = models.CharField(max_length=255, default="")
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)
