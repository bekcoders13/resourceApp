
from models.books import Books
from utils.db_operations import get_in_db, save_in_db


def get_book_f(title, author, db):
    query = db.query(Books)
    if title:
        query = query.filter(Books.title.ilike(f"%{title}%"))
    if author:
        query = query.filter(Books.author.ilike(f"%{author}%"))
    return query


def create_book_f(db, forms):
    for form in forms:
        book = Books(
            title=form.title,
            author=form.author,
            description=form.description,
            publication_date=form.publication_date,
            created_at=form.created_at,
        )
        save_in_db(db, book)


def update_book_f(db, forms):
    for form in forms:
        get_in_db(db, Books, form.ident)
        db.query(Books).filter(Books.id == form.ident).update({
            Books.title: form.title,
            Books.author: form.author,
            Books.description: form.description,
            Books.publication_date: form.publication_date,
            Books.created_at: form.updated_at
        })
        db.commit()


def delete_book_f(db, ident):
    db.query(Books).filter(Books.id == ident).delete()
    db.commit()
