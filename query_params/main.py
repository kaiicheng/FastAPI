# use unicorn to run
# uvicorn hello_fastapi:app --reload

from typing import Optional

from fastapi import FastAPI
import uvicorn

app = FastAPI()

# query parameters

# http://127.0.0.1:8000/users?page_index=3&page_size=20
@app.get('/users')
async def get_users(page_index: int, page_size: int):
    return {"page info": f"index: {page_index} size: {page_size}"}

# optional parameters
# http://127.0.0.1:8000/students?page_index=3
@app.get('/students')
async def get_students(page_index: int, page_size: Optional[int] = 30):
    return {"page info": f"index: {page_index} size: {page_size}"}

# 127.0.0.1:8000/users/1995/friends?page_index=2&page_size=1
# 127.0.0.1:8000/users/1995/friends?page_index=2
@app.get('/users/{user_id}/friends')
async def get_user_friends(page_index: int, user_id: int ,page_size: Optional[int] = 30):
    return {"user friends": f"user id: {user_id}, index {page_index}, size: {page_size}"}


if __name__ == "__main__":

    # equal to uvicorn hello_fastapi:app --reload
    uvicorn.run("main:app", reload=True)
