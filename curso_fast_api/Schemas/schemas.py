from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserDb(UserSchema):
    id: int


class UserSchemaResponse(BaseModel):
    id: int
    username: str
    email: EmailStr


class UserList(BaseModel):
    users: list[UserSchemaResponse]
