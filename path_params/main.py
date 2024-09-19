# use unicorn to run
# uvicorn hello_fastapi:app --reload

from enum import Enum

from fastapi import FastAPI
import uvicorn  

app = FastAPI()



# order of these 2 def matters
# smaller set comes first before broader set

@app.get('/users/current')
async def get_user():
    return {"user": f"This is the current user"}

@app.get('/users/{user_id}')
async def get_user(user_id: int):  # specify type
    return {"user": f"This is the user for {user_id}"}



# dropdown menu
class Gender(str, Enum):
    male = "male"
    female = "female"

@app.get('/students/{gender}')
async def get_user(gender: Gender):
    return {"user": f"This is a {gender.value} student"}

if __name__ == "__main__":

    # equal to uvicorn hello_fastapi:app --reload
    uvicorn.run("main:app", reload=True)
