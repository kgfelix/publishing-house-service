from app.api.entities.base_entity import BaseEntity
from app.api.entities.book import Book
from tinydb import (TinyDB, Query, where)
import json

db = TinyDB('book.json')

class BookRepository(BaseEntity):

    def create(self, book: Book) -> Book:        
        book.id = len(db) + 1 
        db.insert(book.__dict__)
        return book

    def read(self, id: int):
        book_list = db.search(where('id') == id)
        if book_list:
            bookDct = book_list[0]
            book = Book(
                bookDct['id'],
                bookDct['name'],
                bookDct['year'],
                bookDct['authors'],
                bookDct['summary'])
            return book
        else:
            return None

    def read_all(self, name: str):
        data = ''
        if not name:
            data  = db.all()
        else:
            Book = Query()
            book_query = name + '*'
            print(book_query)
            data  = db.search(Book.name.matches(book_query))
        return data

    def update(self, book: Book):
        db.update(book.__dict__, where('id') == book.id)
        return book

    def delete(self, id: int):        
        result = db.remove(where('id') == id)
        return bool(result)
