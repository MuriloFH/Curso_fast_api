import pytest
from fastapi.testclient import TestClient

from curso_fast_api.app import app


@pytest.fixture
def client():  # criando o client, aonde ele vai procurar os endpoints passados nos testes
    return TestClient(app=app)  # Arrange(organização)
