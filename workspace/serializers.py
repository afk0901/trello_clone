from rest_framework import serializers

from workspace.models import Workspace


class WorkspaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Workspace
        fields = ["name"]
