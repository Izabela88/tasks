from task.serializers import TaskSerializer, TileSerializer
from task.models import Task, Tile
from rest_framework import generics


class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    lookup_url_kwarg = "task_id"


class TileList(generics.ListCreateAPIView):
    queryset = Tile.objects.all()
    serializer_class = TileSerializer


class TileDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TileSerializer
    queryset = Tile.objects.all()
    lookup_url_kwarg = "tile_id"
