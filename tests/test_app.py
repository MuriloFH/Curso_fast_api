from http import HTTPStatus


def test_hello_world_return_ok(client):
    response = client.get("/hello_word")  # Act(ação)

    assert response.status_code == HTTPStatus.OK  # Assert(Afirmação)
    assert response.json() == {"message": "Olá Mundo!"}


def test_create_user(client):
    response = client.post("/users/", json={"username": "teste_user", "email": "user@example.com", "password": "pass"})

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {"username": "teste_user", "email": "user@example.com", "id": 1}


def test_read_users(client):
    response = client.get("/users")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"users": [{"username": "teste_user", "email": "user@example.com", "id": 1}]}


def test_read_user(client):
    response = client.get("/users/1")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"username": "teste_user", "email": "user@example.com", "id": 1}


def test_read_user_not_found(client):
    response = client.get("/users/10")

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "User not found"}


def test_update_users(client):
    objectTest = {"username": "teste_user_1", "email": "user@example.com", "password": "pass"}

    objectReturn = {"username": "teste_user_1", "email": "user@example.com", "id": 1}

    response = client.put("/users/1", json=objectTest)

    assert response.status_code == HTTPStatus.OK
    assert response.json() == objectReturn


def test_update_users_not_found(client):
    objectTest = {"username": "teste_user_1", "email": "user@example.com", "password": "pass"}

    response = client.put("/users/2", json=objectTest)

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "User not found"}


def test_delete_user(client):
    response = client.delete("/users/1")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Delete complete"}


def test_delete_user_not_found(client):
    response = client.delete("/users/2")

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "User not found"}
