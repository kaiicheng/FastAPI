# use unicorn to run
# uvicorn main:app --reload

from typing import List, Optional, Set

import uvicorn
from fastapi import FastAPI, Path, Query, Body
from pydantic import BaseModel, Field

app = FastAPI()

# nested model Address in class User(BaseModel)
class Address(BaseModel): 
    address: str
    postcode: str


# multiple request body pydantic model parameter
# pydantic.Field() can validate pydantic model parameter

class User(BaseModel): 
    # username: str
    username: str = Field(..., min_length=3)
    # description: Optional[str] = "default"
    description: Optional[str] = Field(None, max_length=10)
    address: Address  # nested model Address in class User(BaseModel)

class Feature(BaseModel):
    name: str

class Item(BaseModel):
    name: str
    length: int
    # features: List[str]  # typing.List() can specify type of element in list
    features: List[Feature]  # typing.List() can specify type of element in list

# post to create user
@app.post('/carts/{cart_id}')
# if not using fastapi.Body(), count will be query parameter
# async def update_cart(cart_id: int, user: User, item: Item, count: int):
async def update_cart(cart_id: int, user: User, item: Item, count: int = Body(..., ge=2)):
    print(user.username)
    print(item.name)
    result_dict ={
        "cartid": cart_id,
        "username": user.username,
        "itemname": item.name,
        "count": count
    }
    return result_dict


if __name__ == "__main__":

    # equal to uvicorn main:app --reload
    uvicorn.run("main:app", reload=True)
