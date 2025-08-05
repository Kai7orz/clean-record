from sqlalchemy import ForeignKey,Column,Integer,PrimaryKeyConstraint
from pydantic import BaseModel 
from db import Base 

# Records と Categories の中間テーブル
class RecordCategories(Base):
    __tablename__ = 'record_categories'
    __table_args__ = (
        PrimaryKeyConstraint('record_id','category_id'),
    )
    category_id = Column(Integer,ForeignKey('categories.category_id'),nullable=False) 
    record_id = Column(Integer,ForeignKey('records.record_id',ondelete="CASCADE"),nullable=False)

class RecordCategoryCreate(BaseModel):
    category_id: int 

class RecordCategoryResponse(RecordCategoryCreate):
    record_id: int
