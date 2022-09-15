from datetime import date
from typing import List

from pydantic import BaseModel, validator, Field


class Author(BaseModel):
    first_name: str = Field(..., max_length=25)
    last_name: str
    age: int = Field(..., gt=18, lt=90, description='Author age must be more than 18 yo & less than 90 yo')

    # @validator('age')
    # def check_age(cls, v):
    #     if v <= 18 > 90:
    #         raise ValueError('Author age must be more than 18 yo')
    #     return v


class Genre(BaseModel):
    name: str


class Book(BaseModel):
    """Create a table as in Django models"""
    title: str
    writer: str
    duration: str
    data: date
    summary: str
    genres: List[Genre] = []    # set that u can send it free
    pages: int


class BookOut(Book):
    id: int = 2
