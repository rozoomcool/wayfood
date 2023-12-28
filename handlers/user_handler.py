from fastapi import APIRouter, Depends
from sqlmodel import Session

from db import get_session
from models.user import User, UserCreate

router = APIRouter()


@router.get("/")
async def ggg():
    return ""


@router.get("/", response_model=list[User])
async def get_users(session: Session = Depends(get_session())):
    return session.query(User).all()


# @router.post("/")
# async def create_user(user: UserCreate, session: Session = Depends(get_session())):
#     session.add(user)


# @router.get("/{user_id}")
# async def get_user(user_id: int):
#     pass

