from django.db import models
from task.value_objects import TileStatus


class BaseModel(models.Model):
    class Meta:
        abstract = True

    id = models.UUIDField(primary_key=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    modified_at = models.DateTimeField(auto_now_add=True, null=False)


class Tile(BaseModel):
    """Tile object."""
    status = models.CharField(max_length=50, choices=TileStatus.choices())
    launch_date = models.DateTimeField(auto_now_add=True, null=False)

class TaskType(BaseModel):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name  

class Task(BaseModel):
    """Task object."""

    title = models.CharField(max_length=255)
    order = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    tile = models.ForeignKey(Tile, on_delete=models.CASCADE, null=False)
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE, null=False, related_name="tasks")


    def __str__(self):
        return self.title
    
    
    

