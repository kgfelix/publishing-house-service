from abc import (ABC, abstractmethod)

class BaseEntity(ABC):

    @abstractmethod
    def create(self):
        raise NotImplementedError('Method not defined')
    
    @abstractmethod
    def update(self):
        raise NotImplementedError('Method not defined')

    @abstractmethod
    def delete(self):
        raise NotImplementedError('Method not defined')

    @abstractmethod
    def read_all(self):
        raise NotImplementedError('Method not defined')

    @abstractmethod
    def read(self):
        raise NotImplementedError('Method not defined')

    


    



