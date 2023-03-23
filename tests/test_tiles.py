import pytest
from task.models import Tile
from task.value_objects import TileStatus


@pytest.mark.django_db
def test_get_tile_list(create_tile, authorized_client):
    resp = authorized_client.get("/api/tiles/")
    resp_json = resp.json()
    assert resp.status_code == 200
    assert len(resp_json) == 1
    assert resp_json[0]["id"] == str(create_tile.id)


@pytest.mark.django_db
def test_get_tile_detail(create_tile, authorized_client):
    resp = authorized_client.get(f"/api/tiles/{create_tile.id}/")
    resp_json = resp.json()
    assert resp.status_code == 200
    assert resp_json["id"] == str(create_tile.id)


@pytest.mark.django_db
def test_delete_tile(create_tile, authorized_client):
    tile = create_tile
    url = f"/api/tiles/{create_tile.id}/"
    resp = authorized_client.delete(url)
    assert resp.status_code == 204
    assert Tile.objects.filter(id=tile.id).exists() is False


@pytest.mark.django_db
def test_create_tile_successful(authorized_client):
    data = {
        "status": "PENDING",
        "launch_date": "2023-03-22T15:51:53.565658Z",
    }
    url = f"/api/tiles/"
    assert len(Tile.objects.all()) == 0

    resp = authorized_client.post(url, data=data)

    assert resp.status_code == 201
    assert len(Tile.objects.all()) == 1


@pytest.mark.django_db
def test_create_tile_unsuccessful(authorized_client):
    data = {}
    url = f"/api/tiles/"
    assert len(Tile.objects.all()) == 0

    resp = authorized_client.post(url, data=data)

    assert resp.status_code == 400
    assert len(Tile.objects.all()) == 0


def test_tile_update(authorized_client, create_tile):
    tile = create_tile
    data = {
        "status": TileStatus.ARCHIVED,
    }
    url = f"/api/tiles/{create_tile.id}/"
    resp = authorized_client.patch(url, data=data)

    assert resp.status_code == 200
    tile.refresh_from_db()
    assert tile.status == data["status"]
