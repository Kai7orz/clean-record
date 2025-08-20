from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import relationship 
from pydantic import BaseModel 
from db import Base 

# Category テーブル
class Category(Base):
    __tablename__ = 'categories' 
    category_id = Column(Integer,primary_key=True,autoincrement=True,nullable=False) 
    category_name = Column(String(100),nullable=False)
    # このrelationship によって，紐づいたテーブル同士が互いのレコードを参照できるようになる
    records = relationship("Record",secondary="category_records",back_populates="categories")

class CategoryBase(BaseModel):
    category_name: str
    class Config:
        orm_mode = True 
