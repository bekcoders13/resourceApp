from typing import List
from fastapi import APIRouter, Query, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload

from db import database
from functions.books import get_book_f, create_book_f, update_book_f, delete_book_f
from models.books import Books
from models.files import Files
from schemas.books import CreateBook, UpdateBook

books_router = APIRouter(
    prefix="/books",
    tags=["Book operations"]
)


@books_router.get("/get_books")
def get(ident: int = 0, title: str = None,  author: str = None,
        page: int = Query(1), limit: int = Query(25),
        db: Session = Depends(database)):
    if ident:
        db.query(Books).filter(Books.id == ident).first()
        db.query(Books).filter(Books.id == ident).update({
            Books.see_num: Books.see_num + 1
        })
        db.commit()
    query = get_book_f(title, author, db)

    products = (query.options(joinedload(Books.files).load_only(Files.file_path)).
                offset((page - 1) * limit).limit(limit).all())

    return products


@books_router.post('/create')
def create_books(forms: List[CreateBook],
                 db: Session = Depends(database)):
    create_book_f(db, forms)
    raise HTTPException(status_code=200, detail="Create Success!")


@books_router.put("/update")
def update_books(forms: List[UpdateBook], db: Session = Depends(database)):
    update_book_f(db, forms)
    raise HTTPException(status_code=200, detail="Update Success!")


@books_router.delete("/delete")
def delete_books(ident: int = 0, db: Session = Depends(database)):
    delete_book_f(db, ident)
    raise HTTPException(status_code=200, detail="Delete Success!")
