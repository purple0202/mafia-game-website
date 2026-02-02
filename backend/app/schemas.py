from pydantic import BaseModel, EmailStr
from uuid import UUID

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class GameCreate(BaseModel):
    pass

class GameResponse(BaseModel):
    id: UUID
    host_id: UUID
