from sqlalchemy import Column,Integer,String,TIMESTAMP,ForeignKey,DateTime
from sqlalchemy.orm import relationship 
from pydantic import BaseModel 
from sqlalchemy.sql import func
from db import Base 
from typing  import List 
from models.category import Category 
from models.user import User
from models.image import Image

# Recrods テーブル
class Record(Base):
    __tablename__ = 'records'
    record_id = Column(Integer,primary_key=True,autoincrement=True) 
    recorded_at = Column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    record_name = Column(String(254),nullable=False)
    user_id = Column(Integer,ForeignKey("users.user_id",ondelete="CASCADE"),nullable=False)

    categories = relationship("Category",secondary="category_records",back_populates="records")
    images = relationship("Image",back_populates="record")
    user = relationship("User",back_populates="records")

class RecordBase(BaseModel):
    record_name: str
    user_id: int 
    category_id: int 

class RecordOutput(RecordBase):
    record_id: int 
    recorded_at: DateTime
    images: List[Image]
    categories: List[Category]
    
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True 