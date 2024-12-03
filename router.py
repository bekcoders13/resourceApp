from fastapi import APIRouter

from db import engine, Base
from routes.books import books_router
from routes.files import files_router

api = APIRouter()


Base.metadata.create_all(bind=engine)

api.include_router(books_router)
api.include_router(files_router)
