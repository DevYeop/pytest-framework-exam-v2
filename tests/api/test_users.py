import pytest
from core.api.api_client import APIClient

@pytest.fixture
def api():
    return APIClient("https://jsonplaceholder.typicode.com")

def test_get_users_status_code(api):
    response = api.get("/users")
    # 가장 기본이 되는 상태 코드 200 검증
    assert response.status_code == 200