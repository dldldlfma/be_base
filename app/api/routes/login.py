from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user import UserLogin, UserRead
from app.crud.user import get_user_by_email, verify_password
from app.db.session import get_db

router = APIRouter(prefix="/login", tags=["login"])

@router.post("/", response_model=UserRead)
async def login_user(
    user_in: UserLogin,
    db: AsyncSession = Depends(get_db)
):
    existing_user = await get_user_by_email(db, user_in.email)

    if not existing_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Check Email or Password"
        )

    if not verify_password(user_in.password, existing_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Check Email or Password"
        )
    return existing_user
