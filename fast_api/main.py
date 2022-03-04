from typing import List
from uuid import UUID
from fastapi import FastAPI, HTTPException
from models import Gender, Role, User, UserUpdateRequest

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("fa6cca01-3b6a-4948-908c-6242eba0f466"),
        first_name="John",
        last_name="Doe",
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    ),
    User(
        id=UUID("e21d74f9-555b-45c0-b0dd-a592cb95821d"),
        first_name="Jane",
        last_name="Rosemary",
        gender=Gender.female,
        roles=[Role.user]
    )
]


@app.get('/api/v1/users')
async def fetch_users():
    return db


@app.get('/api/v1/users/{user_id}')
async def fetch_single_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            return user


@app.post('/api/v1/users')
async def create_user(user: User):
    db.append(user)
    return {"id": user.id}


@app.put('/api/v1/users/{user_id}')
async def update_user(user_update: UserUpdateRequest, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return {"message": f"User {user.id} successfully updated!"}
    raise HTTPException(
        status_code=404,
        detail=f"User {user_id} not found!"
    )


@app.delete('/api/v1/users/{user_id}')
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return {"message": f"User {user.id} successfully deleted!"}
    raise HTTPException(
        status_code=404,
        detail=f"User {user_id} not found!"
    )
