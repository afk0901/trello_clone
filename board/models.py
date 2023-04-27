from django.db import models

from workspace.models import Workspace


class Board(models.Model):
    """
    Board that each workspace owns.
    Each workspace can have many boards.
    """

    name = models.CharField(max_length=255, default="")
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)
