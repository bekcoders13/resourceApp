from sqlalchemy import Column, Integer, String, Text, Date
from db import Base


class Books(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    publication_date = Column(Integer, nullable=False)
    created_at = Column(Date, nullable=False)
    see_num = Column(Integer, default=0)
    quantity = Column(Integer, default=0)
