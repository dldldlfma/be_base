# app/api/routes/user.py

from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user import UserCreate, UserRead
from app.crud.user import create_user, get_user_by_email, get_user_by_id
from app.db.session import get_db

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserRead)
async def register_user(
    user_in: UserCreate,
    db: AsyncSession = Depends(get_db)
):
    existing_user = await get_user_by_email(db, user_in.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    new_user = await create_user(db, user_in)
    return new_user

@router.get("/", response_model=UserRead)
async def get_user_byid(    # Change Function Name 
    user_id: int = Query(...),
    db: AsyncSession = Depends(get_db)
):
    existing_user = await get_user_by_id(db, user_id)
    if existing_user:
        return existing_user
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="ID Not found"
        )