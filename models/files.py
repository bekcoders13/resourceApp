from sqlalchemy import Column, Integer, Text, Double, Date
from sqlalchemy.orm import relationship, backref

from db import Base
from models.books import Books


class Files(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer, nullable=False)
    file_path = Column(Text, nullable=False)
    file_size = Column(Double, nullable=False)
    created_at = Column(Date, nullable=False)

    book = relationship("Books", foreign_keys=[book_id],
                        primaryjoin=lambda: Books.id == Files.book_id,
                        backref=backref("files"))
