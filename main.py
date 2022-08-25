from typing import List
from fastapi import FastAPI, HTTPException
from models import User, Gender

app = FastAPI()

db: List[User] = [
    User(
        id=1,
        first_name="Murilo",
        last_name="Machado",
        gender=Gender.male
    ),

    User(
        id=2,
        first_name="Maria",
        last_name="Oliveira",
        gender=Gender.female
    ),

    User(
        id=3,
        first_name="Jack",
        last_name="Cliver",
        gender=Gender.male
    )
]

@app.get("/users")
async def get_users():
    return db

@app.get("/users/{id_user}")
async def get_users_by_id(id_user: int):
    for user in db:
        if user.id == id_user:
            return user
    raise HTTPException(
        status_code=500,
        detail="Error 500: User doesn't exist."
    )

@app.post("/users")
async def post_users(user: User):
    db.append(user)
    return "You put the user successfully."

@app.delete("/users/{id_user}")
async def delete_users(id_user: int):
    for user in db:
        if user.id == id_user:
            db.remove(user)
            return "You remove the user successfully."
        raise HTTPException(
            status_code=500,
            detail="Error 500: User doesn't exist."
        )

