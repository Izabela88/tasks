from rest_framework import serializers
from task.models import Task, Tile


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
        read_only_fields = ("id",)


class TileSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(read_only=True, many=True)

    class Meta:
        model = Tile
        fields = (
            "id",
            "status",
            "launch_date",
            "created_at",
            "modified_at",
            "tasks",
        )
        read_only_fields = ("id", "tasks")
