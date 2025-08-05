from sqlalchemy import Column,Integer,String,TIMESTAMP
from sqlalchemy.orm import relationship 
from sqlalchemy.schema import FetchedValue
from pydantic import BaseModel 
from db import Base 

# Recrods テーブル
class Records(Base):
    __tablename__ = 'records'
    record_id = Column(Integer,primary_key=True,autoincrement=True) 
    recorded_date = Column(TIMESTAMP,FetchedValue())
    record_name = Column(String(254),nullable=False) 
    categories = relationship("Categories",secondary="record_categories",back_populates="records")
    images = relationship("Images")

class RecordCreate(BaseModel):
    record_name: str

class RecordResponse(RecordCreate):
    record_id: int 
    recorded_date: TIMESTAMP

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True 