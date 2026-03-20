from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(title="Book API")


class Book(BaseModel):
    id: int
    title: str
    author: str
    in_stock: bool = True


books = [
    {"id": 1, "title": "Python Basics", "author": "M. Lee", "in_stock": True},
    {"id": 2, "title": "FastAPI Projects", "author": "A. Smith", "in_stock": False},
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the Book API"}


# Task 1:
# Add a GET /books route that returns all books.
# Add a GET /books/{book_id} route that returns a single book.


# Task 2:
# Add a POST /books route that accepts a Book object and stores it.
# Add a DELETE /books/{book_id} route that removes a book by id.