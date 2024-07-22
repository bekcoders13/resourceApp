from datetime import date
from pydantic import BaseModel, Field


class CreateBook(BaseModel):
    title: str
    author: str
    description: str
    publication_date: int
    created_at: date

    # class Config:
    #     orm_mode = True


class UpdateBook(BaseModel):
    ident: int = Field(..., gt=0)
    title: str
    author: str
    description: str
    publication_date: int
    updated_at: date
