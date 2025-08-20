from sqlalchemy import Table,ForeignKey,Column,Integer,PrimaryKeyConstraint
from pydantic import BaseModel 
from db import Base 

# 中間テーブル
class CategoryRecord(Base):
    __tablename__='category_records'
    category_id = Column(ForeignKey('categories.category_id'),primary_key=True)
    record_id = Column(ForeignKey('records.record_id'),primary_key=True)
