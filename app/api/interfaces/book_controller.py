from typing import List
from pydantic import parse_obj_as
from app.api.interfaces.book_model import (BookIn, BookOut)
from app.api.entities.book import Book
from app.api.entities.base_entity import BaseEntity
from app.api.infrastructure.book_repository import BookRepository

class BookController(object):

    def __init__(self, repository: BaseEntity):
        self.repository = repository

    def create(self, bookIn: BookIn) -> BookOut:
        book = Book(
            0, 
            bookIn.name,
            bookIn.year,
            bookIn.authors,
            bookIn.summary)
        book = book.createBook(self.repository)
        book_out = BookOut.from_orm(book)
        return book_out

    def read_all(self, name) -> List[BookOut]:
        book = Book()
        books = book.listAllBooks(name, self.repository)
        book_out_list = parse_obj_as(List[BookOut], books)
        return book_out_list

    def update(self, id: int, bookIn: BookIn) -> BookOut:
        book = Book(
            id, 
            bookIn.name,
            bookIn.year,
            bookIn.authors,
            bookIn.summary)
        book = book.updateBook(id, self.repository)
        book_out = BookOut.from_orm(book)
        return book_out

    def read(self, id: int) -> BookOut:
        book = Book()
        book = book.getOneBook(id, self.repository)
        if book:
            return BookOut.from_orm(book)
        return book

    def delete(self, id: int) -> bool:
        book = Book()
        result = book.deleteBook(id, self.repository)
        return result
