import pytest


def test_get_users_status_code(api):
    response = api.get("/users")
    assert response.status_code == 200

def test_get_single_user(api):
    response = api.get("/users/1")
    assert response.status_code == 200