# use unicorn to run
# uvicorn main:app --reload

from fastapi import FastAPI, Path, Query
import uvicorn  

app = FastAPI()

# Path validation

# parameter validation for path parameters
# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/users/80000
# http://127.0.0.1:8000/users/0
@app.get('/users/{user_id}')
async def get_user(user_id: int = Path(..., title="User ID", ge=1, le=1000)):
    return {"user": f"This is the user for {user_id}"}

# parameter validation for path parameters
# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/books/abc
@app.get('/books/{book_name}')
async def get_book(book_name: str = Path(..., title="Book Name", min_length=3, max_length=10)):
    return {"Book Info": f"This is a book for {book_name}"}

# parameter validation for path parameters
# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/books/abc
# http://127.0.0.1:8000/users/0
@app.get('/items/{item_no}')
async def get_item(item_no: str = Path(..., title="Item No", regex='^[a|b|c]-[\\d]*$')):
    return {"Item Info": f"This is an item for {item_no}"}


# Query validation

# parameter validation for path parameters
# http://127.0.0.1:8000/docs#/default/get_users_users_get
# http://127.0.0.1:8000/users
# http://127.0.0.1:8000/users?page_index=2
# http://127.0.0.1:8000/users?page_index=299999
# http://127.0.0.1:8000/users?page-index=4
@app.get('/users')
async def get_users(page_index: int = Query(1, alias='page-index', title="Page Index", ge=1, le=1000)):
    return {"user": f'Index: {page_index}'}

# # parameter validation for path parameters
# # http://127.0.0.1:8000/docs
# # http://127.0.0.1:8000/books/abc
@app.get('/books')
async def get_books(book_name: str = Query("abc book", title="Book Name", min_length=3, max_length=10)):
    return {"Book Info": f"This is a book for {book_name}"}

# # parameter validation for path parameters
# # http://127.0.0.1:8000/docs
# # http://127.0.0.1:8000/books/abc
# # http://127.0.0.1:8000/users/0
@app.get('/items')
async def get_items(item_no: str = Query("abc item", title="Item No", regex='^[a|b|c]-[\\d]*$')):
    return {"Item Info": f"This is an item for {item_no}"}


if __name__ == "__main__":

    # equal to uvicorn main:app --reload
    uvicorn.run("main:app", reload=True)
