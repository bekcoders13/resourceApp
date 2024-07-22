from fastapi import APIRouter

from routes.books import books_router
from routes.files import files_router
api = APIRouter()

api.include_router(books_router)
api.include_router(files_router)
