from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.user import UserRegister
from app.models.user import User
from app.database.dependencies import get_db
from app.services.auth_service import hash_password

router = APIRouter()


@router.post("/register")
def register_user(
    user: UserRegister,
    db: Session = Depends(get_db)
):
    try:
        hashed_password = hash_password(user.password)

        new_user = User(
            name=user.name,
            email=user.email,
            password_hash=hashed_password
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return {
            "message": "User Registered Successfully"
        }

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )