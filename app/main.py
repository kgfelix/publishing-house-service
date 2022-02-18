from fastapi import (FastAPI, HTTPException)
from typing import List
from app.api.interfaces.book_controller import BookController
from app.api.interfaces.book_model import (BookIn, BookOut)
from app.api.infrastructure.book_repository import BookRepository

app = FastAPI(title="Book Service")

bookRepository = BookRepository()
bookController = BookController(bookRepository)

@app.get("/")
def hello():
    return {"message":"It is a health check message"}

@app.post('/api/v1/books/', response_model=BookOut, status_code=201)
def create(payload: BookIn):
    bookOut = bookController.create(payload)
    if not bookOut:
        raise HTTPException(status_code=404, detail="Error creating a new book")
    return bookOut

@app.get('/api/v1/books/', response_model=List[BookOut], status_code=201)
def read_all(name: str = None):
    return bookController.read_all(name)

@app.get('/api/v1/books/{id}', response_model=BookOut)
def read(id: int):
    book = bookController.read(id)
    if not book:
        raise HTTPException(status_code=404, detail=f"Book {id} not found")
    return book

@app.put('/api/v1/books/{id}', response_model=BookOut)
def update(id: int, payload: BookIn):
    bookOut = bookController.update(id, payload)
    if not bookOut:
        raise HTTPException(status_code=404, detail=f"Error updating book {id}")
    return bookOut

@app.delete('/api/v1/books/{id}')
def delete(id: int):
    response = bookController.delete(id)
    if not response:
        raise HTTPException(status_code=404, detail=f"Book {id} not found")
    return {"result": response}

