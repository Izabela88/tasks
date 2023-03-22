from django.urls import path

from task.views import TaskDetail, TaskList, TileDetail, TileList

urlpatterns = [
    path("tasks/", TaskList.as_view(), name="task_list"),
    path("tasks/<uuid:task_id>/", TaskDetail.as_view(), name="task_detail"),
    path("tiles/", TileList.as_view(), name="tile_list"),
    path("tiles/<uuid:tile_id>/", TileDetail.as_view(), name="tile_detail"),
]
