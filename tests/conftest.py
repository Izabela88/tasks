import datetime

import pytest
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from task.models import Task, TaskType, Tile
from task.value_objects import TileStatus


@pytest.fixture
def authorized_client(create_user):
    refresh = RefreshToken.for_user(create_user)
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
    return client


@pytest.fixture
def create_user(django_user_model):
    user = django_user_model.objects.create_user(
        username="test", password="test", is_superuser=True
    )
    return user


@pytest.fixture
def create_task_type():
    task_type = TaskType.objects.create(name="Test name")
    return task_type


@pytest.fixture
def create_tile():
    tile = Tile.objects.create(
        status=TileStatus.PENDING,
        launch_date=datetime.datetime.utcnow(),
        created_at=datetime.datetime.utcnow(),
        modified_at=datetime.datetime.utcnow(),
    )
    return tile


@pytest.fixture
def create_task(create_tile, create_task_type):
    task = Task.objects.create(
        title="Example title",
        description="Example description",
        order="AAA-000",
        tile=create_tile,
        created_at=datetime.datetime.utcnow(),
        modified_at=datetime.datetime.utcnow(),
        task_type=create_task_type,
    )
    return task
