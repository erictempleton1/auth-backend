from typing import List
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class User(BaseModel):
    username: str


@router.get('/users/', response_model=List[User], tags=['users'])
async def read_users() -> List[User]:
    return [{'username': 'Foo'}, {'username': 'Bar'}]


@router.get('users/{username}', response_model=User, tags=['users'])
async def read_user(username: str) -> User:
    return {'username': username}
