from sqlalchemy import Column,Integer,String,TIMESTAMP,DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from pydantic import BaseModel 
from db import Base 


# Users テーブル
# SQLAlchemy のモデル
class User(Base): 
    __tablename__ = 'users'
    user_id = Column(Integer,primary_key=True,autoincrement=True)
    user_name = Column(String(30),nullable=False) 
    email = Column(String(254),nullable=False)
    age = Column(Integer,nullable=False)
    created_at = Column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    records = relationship("Record",back_populates="user")

# Pydantic のモデル（リクエスト用）
class UserCreate(BaseModel):
    user_name: str
    email: str 
    age: int 

# Pydantic のモデル（レスポンス用）
class UserResponse(UserCreate):
    id: int
    created_at: DateTime
    class Config:
        orm_mode = True
        # TIMESTAMP が pydantic では定義されていないため，下記記述がないとTestUserResponse のcreated_at のvalidation でエラーとなる
        arbitrary_types_allowed = True