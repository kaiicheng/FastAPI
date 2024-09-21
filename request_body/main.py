# use unicorn to run
# uvicorn main:app --reload

from typing import Optional
from enum import Enum

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Gender(str, Enum):
    male = 'male'
    female = 'female'

class UserModel(BaseModel):
    username: str
    description: Optional[str] = "default"
    gender: Gender

# post to create user
@app.post('/users')
async def create_users(user_model: UserModel):
    print(user_model.username)
    user_dict = user_model.model_dump()

    return user_dict

# put to update user
@app.put('/users/{user_id}')
async def update_users(user_id: int, user_model: UserModel):
    print(user_model.username)
    user_dict = user_model.model_dump()
    user_dict.update({'id': user_id})

    return user_dict

if __name__ == "__main__":

    # equal to uvicorn main:app --reload
    uvicorn.run("main:app", reload=True)
