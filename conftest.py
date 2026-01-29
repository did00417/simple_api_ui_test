import pytest
from core.api.api_client import APIClient

@pytest.fixture
def api():
    return APIClient("https://jsonplaceholder.typicode.com")