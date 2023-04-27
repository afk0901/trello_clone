from rest_framework import viewsets

from workspace.models import Workspace
from workspace.serializers import WorkspaceSerializer


class WorkspaceViewSet(viewsets.ReadOnlyModelViewSet):
    """
    All the workspaces that belongs to the authenticated user.
    """

    serializer_class = WorkspaceSerializer

    def get_queryset(self):
        return Workspace.objects.get_workspaces_by_user(self.request.user)
