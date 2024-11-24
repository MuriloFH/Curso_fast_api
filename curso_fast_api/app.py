from http import HTTPStatus

from fastapi import FastAPI, HTTPException

from curso_fast_api.Schemas.schemas import (
    Message,
    UserDb,
    UserList,
    UserSchema,
    UserSchemaResponse,
)

app = FastAPI()

fake_db = []


@app.get("/hello_word", status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {"message": "Olá Mundo!"}


@app.post("/users/", status_code=HTTPStatus.CREATED, response_model=UserSchemaResponse)
def post_users(user: UserSchema):
    user_with_id = UserDb(
        id=len(fake_db) + 1,
        **user.model_dump(),  # transforma o user que está em schema para dict
    )
    fake_db.append(user_with_id)
    return user_with_id


@app.get("/users/", status_code=HTTPStatus.OK, response_model=UserList)
def read_users():
    return {"users": fake_db}


@app.get("/users/{user_id}", status_code=HTTPStatus.OK, response_model=UserSchemaResponse)
def read_user(user_id: int):
    if user_id < 1 or user_id > len(fake_db):
        raise HTTPException(detail="User not found", status_code=HTTPStatus.NOT_FOUND)

    for i, value in enumerate(fake_db):
        if value.id == user_id:
            user_found = value

    return user_found


@app.put("/users/{user_id}", status_code=HTTPStatus.OK, response_model=UserSchemaResponse)
def update_user(user_id: int, user: UserSchema):
    if user_id < 1 or user_id > len(fake_db):
        raise HTTPException(detail="User not found", status_code=HTTPStatus.NOT_FOUND)

    user_with_id = UserDb(
        id=user_id,
        **user.model_dump(),  # transforma o user que está em schema para dict
    )

    fake_db[user_id - 1] = user_with_id

    return fake_db[user_id - 1]


@app.delete("/users/{user_id}", status_code=HTTPStatus.OK, response_model=Message)
def delete_user(user_id: int):
    if user_id < 1 or user_id > len(fake_db):
        raise HTTPException(detail="User not found", status_code=HTTPStatus.NOT_FOUND)

    for i, value in enumerate(fake_db):
        if value.id == user_id:
            del fake_db[i]

    return {"message": "Delete complete"}
