from rest_framework import generics, permissions

from task.models import Task, Tile
from task.serializers import TaskSerializer, TileSerializer


class TaskList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    lookup_url_kwarg = "task_id"


class TileList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Tile.objects.all()
    serializer_class = TileSerializer


class TileDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = TileSerializer
    queryset = Tile.objects.all()
    lookup_url_kwarg = "tile_id"
