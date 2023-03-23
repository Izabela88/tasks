import pytest
from rest_framework.test import APIClient

from task.models import Task


@pytest.mark.django_db
def test_get_task_list(create_task, authorized_client):
    resp = authorized_client.get("/api/tasks/")
    resp_json = resp.json()
    assert resp.status_code == 200
    assert len(resp_json) == 1
    assert resp_json[0]["id"] == str(create_task.id)


@pytest.mark.django_db
def test_get_task_detail(create_task, authorized_client):
    resp = authorized_client.get(f"/api/tasks/{create_task.id}/")
    resp_json = resp.json()
    assert resp.status_code == 200
    assert resp_json["id"] == str(create_task.id)


@pytest.mark.django_db
def test_user_is_not_authenticated():
    client = APIClient()
    resp_tasks = client.get("/api/tasks/")
    resp_task_detail = client.get(
        "/api/tasks/712b7fd0-88c2-476f-a379-e38cc23af608/"
    )
    resp_tiles = client.get("/api/tiles/")
    resp_tile_detail = client.get(
        "/api/tiles/712b7fd0-88c2-476f-a379-e38cc23af444/"
    )
    assert resp_tasks.status_code == 401
    assert resp_task_detail.status_code == 401
    assert resp_tiles.status_code == 401
    assert resp_tile_detail.status_code == 401


@pytest.mark.django_db
def test_delete_task(create_task, authorized_client):
    task = create_task
    url = f"/api/tasks/{create_task.id}/"
    resp = authorized_client.delete(url)
    assert resp.status_code == 204
    assert Task.objects.filter(id=task.id).exists() is False


@pytest.mark.django_db
def test_create_task_successful(
    authorized_client, create_tile, create_task_type
):
    data = {
        "title": "Test",
        "order": "Test Order",
        "description": "Description Test",
        "tile_id": create_tile.id,
        "task_type": create_task_type,
    }
    url = "/api/tasks/"
    assert len(Task.objects.all()) == 0

    resp = authorized_client.post(url, data=data)

    assert resp.status_code == 201
    assert len(Task.objects.all()) == 1


@pytest.mark.django_db
def test_create_task_unsuccessful(authorized_client):
    data = {
        "title": "Test",
        "order": "Test Order",
        "description": "Description Test",
        "tile_id": "",
        "task_type": "",
    }
    url = "/api/tasks/"
    assert len(Task.objects.all()) == 0

    resp = authorized_client.post(url, data=data)

    assert resp.status_code == 400
    assert len(Task.objects.all()) == 0


def test_partial_task_update(authorized_client, create_task):
    task = create_task
    data = {
        "description": "New Description Test",
    }
    url = f"/api/tasks/{create_task.id}/"
    resp = authorized_client.patch(url, data=data)
    assert resp.status_code == 200
    task.refresh_from_db()
    assert task.description == data["description"]


def test_full_task_update(
    authorized_client, create_task, create_tile, create_task_type
):
    task = create_task
    data = {
        "title": "New Test",
        "order": "New Test Order",
        "description": "New Description Test",
        "tile_id": create_tile.id,
        "task_type": create_task_type,
    }
    url = f"/api/tasks/{create_task.id}/"
    resp = authorized_client.put(url, data=data)
    assert resp.status_code == 200
    task.refresh_from_db()
    assert task.title == data["title"]
    assert task.order == data["order"]
    assert task.description == data["description"]
    assert task.tile.id == data["tile_id"]
    assert task.task_type == data["task_type"]
