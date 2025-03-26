from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCrate(BaseModel):
    email: EmailStr
    password: str
    name: str

class UserRead(BaseModel):
    id: int
    email: EmailStr
    name: str
    registered_at: datetime

    class Config:
        orm_mode=True

class UserInDB(UserRead):
    hashed_password: str
