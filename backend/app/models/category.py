from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import relationship 
from pydantic import BaseModel 
from db import Base 

# Categories テーブル
class Categories(Base):
    __tablename__ = 'categories' 
    category_id = Column(Integer,primary_key=True,autoincrement=True,nullable=False) 
    category_name = Column(String(100),nullable=False)
    # このrelationship によって，紐づいたテーブル同士が互いのレコードを参照できるようになる
    records = relationship("Records",secondary="record_categories",back_populates="categories")

class CategoryCreate(BaseModel):
    category_name: str

class CategoryResponse(CategoryCreate):
    category_id:int 

