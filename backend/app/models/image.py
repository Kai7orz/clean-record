from typing import Optional
from sqlalchemy import ForeignKey,Column,Integer,String
from sqlalchemy.orm import relationship 
from pydantic import BaseModel 
from db import Base 

# Images テーブル
class Image(Base):
    __tablename__ = 'images'
    record_id = Column(Integer,ForeignKey('records.record_id',ondelete="CASCADE"))
    image_id = Column(Integer,primary_key=True,autoincrement=True)
    image_url = Column(String(2048),nullable=False)
    image_description = Column(String(1024),nullable=True)

    record = relationship("Record",back_populates="images")

class ImageCreate(BaseModel):
    record_id: int 
    image_url: str
    image_description: Optional[str] = None

class ImageResponse(ImageCreate):
    image_id: int 
    record_id: int 

    class Config:
        orm_mode = True 
        arbitrary_types_allowed = True