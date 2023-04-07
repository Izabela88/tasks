from rest_framework import serializers

from task.models import Task, Tile, TaskType


class TaskSerializer(serializers.ModelSerializer):
    tile_id = serializers.UUIDField(required=True)

    class Meta:
        model = Task
        exclude = ("tile",)
        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )


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
        read_only_fields = (
            "id",
            "tasks",
            "created_at",
            "updated_at",
        )


class TaskTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskType
        fields = "__all__"
