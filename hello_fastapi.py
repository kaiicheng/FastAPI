# use unicorn to run
# uvicorn hello_fastapi:app reload

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def hello_fastapi():
    return {'message': "Hello FastAPI from root!"}

@app.get('/hellofastapi')
async def hello_fastapi():
    return {'message': "Hello FastAPI from ./hellofastapi!"}
