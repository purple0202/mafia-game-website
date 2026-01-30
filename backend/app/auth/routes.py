from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas import UserCreate
from app.models import User
from app.auth.security import hash_password

router = APIRouter()

@router.post("/register")
async def register(user: UserCreate, db: AsyncSession = Depends(get_db)):
    new_user = User(
        email=user.email,
        password_hash=hash_password(user.password)
    )
    db.add(new_user)
    await db.commit()
    return {"status": "ok"}
