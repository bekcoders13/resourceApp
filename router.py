from fastapi import APIRouter

import models
from db import engine
from routes.books import books_router
from routes.files import files_router
api = APIRouter()


models.books.Base.metadata.create_all(bind=engine)
models.files.Base.metadata.create_all(bind=engine)

api.include_router(books_router)
api.include_router(files_router)
