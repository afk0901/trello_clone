from django.db import models
from django.db.models import QuerySet

from user.models import User


class WorkspaceManager(models.Manager):
    @staticmethod
    def get_workspaces_by_user(user: User) -> QuerySet:
        return Workspace.objects.filter(user=user)


class Workspace(models.Model):
    """
    Trello Workspace model that the user owns.
    Each user can have many Workspaces.
    """

    name = models.CharField(max_length=255, default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    objects = WorkspaceManager()
