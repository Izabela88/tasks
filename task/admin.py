from django.contrib import admin

from task.models import Task, TaskType, Tile


class TaskAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "order",
        "description",
        "tile_id",
        "task_type",
    ]


class TileAdmin(admin.ModelAdmin):
    list_display = [
        "status",
        "launch_date",
    ]


class TaskTypeAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]


admin.site.register(Task, TaskAdmin)
admin.site.register(Tile, TileAdmin)
admin.site.register(TaskType, TaskTypeAdmin)
