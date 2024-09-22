# use unicorn to run
# uvicorn main:app --reload

from typing import Optional, List, Set, Union

import uvicorn
from fastapi import FastAPI, Path, Query, Body, Cookie, Header, Request, Response, HTTPException, status, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from sqlalchemy import create_engine, String, Integer, select
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Mapped, mapped_column


async def set_charset():
    print("set UTF-8")


app = FastAPI(dependencies=[Depends(set_charset)])


# get_items() depends on pageinfo_params(), pageinfo_params() depends on total_param
# get_items() depends on PageInfo class, PageInfo class depends on total_param


# verify user, @app.get('/users') need authentication
async def verify_auth(api_token: Optional[str] = Header(None, alias="api-token")):
    if not api_token:
        raise HTTPException(status_code=400, detail="Unauthorized")


def total_param(total_page: Optional[int] = 1):
    return total_page


# only need to define public pageinfo_params function once and all app can use
def pageinfo_params(page_index: Optional[int] = 1, page_size: Optional[int] = 10,
                    total: Optional[int] = Depends(total_param)):
    return {"page_index": page_index, "page_size": page_size, "total": total}


# class could be the target of depends function
class PageInfo:
    def __init__(self, page_index: Optional[int] = 1, page_size: Optional[int] = 10,
                 total: Optional[int] = Depends(total_param)):
        self.page_index = page_index
        self.page_size = page_size
        self.total = total


@app.get('/items')
# async def get_items(page_index: Optional[int] = 1, page_size: Optional[int] = 10):  # moved to pageinfo_params function
async def get_items(page_info: dict = Depends(pageinfo_params)):  # use Depends() injection to call pageinfo_params function

    # return {"page_index": page_index, "page_size": page_size}

    return {"page_index": page_info.get("page_index"),
            "page_size": page_info.get("page_size"),
            "total": page_info.get("total")}


# @app.get('/users') need verify_auth() function, then depends on it
@app.get('/users', dependencies=[Depends(verify_auth)])
async def get_users(page_info: PageInfo = Depends(PageInfo)):

    return {"page_index": page_info.page_index,
            "page_size": page_info.page_size,
            "total": page_info.total}


@app.get('/goods')
# can call class PageInfo for injection
async def get_users(page_info: PageInfo = Depends()):

    return {"page_index": page_info.page_index, "page_size": page_info.page_size}


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)