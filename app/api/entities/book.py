from app.api.entities.base_entity import BaseEntity


class Book(object):
    def __init__(self, id: int = None, name: str = None, year: int = None, authors: str = None, summary: str = None):
        self.id = id
        self.name = name
        self.year = year
        self.authors = authors
        self.summary = summary

    def createBook(self, repository: BaseEntity):
        repository.create(self)
        return self

    def listAllBooks(self, name: str, repository: BaseEntity):
        book_list = repository.read_all(name)
        return book_list

    def getOneBook(self, id: int, repository: BaseEntity):        
        book = repository.read(id)
        return book

    def updateBook(self, id: int, repository: BaseEntity):
        repository.update(self)
        return self

    def deleteBook(self, id: int, repository: BaseEntity):
        result = repository.delete(id)
        return result
