from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str
    role: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class BookBase(BaseModel):
    title: str
    description: str
    publication_date: date
    available_copies: int

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int
    authors: List['Author']

    class Config:
        orm_mode = True

class AuthorBase(BaseModel):
    name: str
    biography: str
    birth_date: date

class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    id: int
    books: List[Book]

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class Login(BaseModel):
    username: str
    password: str
