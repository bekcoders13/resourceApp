import os
import shutil
from datetime import datetime

from models.books import Books
from models.files import Files
from utils.db_operations import get_in_db
from utils.file_size_f import get_file_size


async def create_file_f(book_id, file_path, db):
    get_in_db(db, Books, book_id)
    uploaded_file_objects = []
    cover_file_path = f"files/{file_path.filename}"
    with open(cover_file_path, "wb") as file_object:
        shutil.copyfileobj(file_path.file, file_object)

    file_model = Files(
        book_id=book_id,
        file_path=file_path.filename,
        created_at=datetime.utcnow(),
        file_size=get_file_size(cover_file_path)
    )
    uploaded_file_objects.append(file_model)
    db.add_all(uploaded_file_objects)
    db.commit()


async def delete_file_f(ident, db):
    get_in_db(db, Files, ident)
    db_books = db.query(Files).all()
    db_file_book = db.query(Files).filter(Files.id == ident).first()
    db.delete(db_file_book)
    db.commit()
    # delete files in dir
    for file in db_books:
        if db_file_book.file_path == file.file_path:
            break
    else:
        os.remove(f"files/{db_file_book.file_path}")
