from django.db import models

from board.models import Board


class List(models.Model):
    name = models.CharField(max_length=255, default="")
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
