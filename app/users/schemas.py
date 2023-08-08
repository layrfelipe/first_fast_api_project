from pydantic import BaseModel

class User(BaseModel):
    username: str

class UserInDB(BaseModel):
    username: str
    password: str
