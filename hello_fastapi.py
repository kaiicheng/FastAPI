# use unicorn to run
# uvicorn hello_fastapi:app --reload

import uvicorn

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def hello_fastapi():
    return {'message': "Hello FastAPI from root!"}

@app.get('/hellofastapi')
async def hello_fastapi():
    return {'message': "Hello FastAPI from ./hellofastapi!"}

if __name__ == "__main__":

    # equal to uvicorn hello_fastapi:app --reload
    uvicorn.run("helloworld:app", reload=True)
