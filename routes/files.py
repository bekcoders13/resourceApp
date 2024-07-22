import os
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy import desc
from sqlalchemy.orm import Session
from starlette.responses import FileResponse

from functions.files import create_file_f, delete_file_f
from db import database
from models.files import Files

files_router = APIRouter(prefix="/files", tags=["Files operations"])

# pdf file operations


@files_router.get("/download_file")
async def download_file(filename: str):
    file_path = f"./files/{filename}"
    if os.path.exists(file_path):
        return FileResponse(file_path)
    else:
        return {"error": "File not found"}


@files_router.get("/get_files")
async def get(db: Session = Depends(database)):
    return db.query(Files).order_by(desc(Files.id)).all()


@files_router.post("/create_file")
async def create(book_id: int, file_path: UploadFile = File(...),
                 db: Session = Depends(database)):
    await create_file_f(book_id, file_path, db)
    raise HTTPException(200, "Create Success!")


@files_router.delete("/delete_file")
async def delete(ident: int, db: Session = Depends(database)):
    await delete_file_f(ident, db)
    raise HTTPException(200, "Delete Success!")
