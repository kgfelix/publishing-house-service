from typing import List
from pydantic import BaseModel

class BookIn(BaseModel):    
    name: str
    year: int
    authors: List[str]
    summary: str

class BookOut(BookIn):
    id: int

    class Config:
        orm_mode = True
