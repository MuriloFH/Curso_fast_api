from http import HTTPStatus

from fastapi.testclient import TestClient

from curso_fast_api.app import app


def test_read_root_return_ok():
    client = TestClient(app)  # Arrange(organização)

    response = client.get("/")  # Act(ação)

    assert response.status_code == HTTPStatus.OK  # Assert(Afirmação)
    assert response.json() == {"message": "Olá Mundo!"}
