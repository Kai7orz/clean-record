from sqlalchemy import Column,Integer,String,TIMESTAMP
from sqlalchemy.schema import FetchedValue
from pydantic import BaseModel 
from db import Base 

# Users テーブル
# SQLAlchemy のモデル
class Users(Base): 
    __tablename__ = 'users'
    user_id = Column(Integer,primary_key=True,autoincrement=True)
    user_name = Column(String(30),nullable=False) 
    email = Column(String(254),nullable=False)
    age = Column(Integer,nullable=False)
    created_at = Column(TIMESTAMP,FetchedValue())

# Pydantic のモデル（リクエスト用）
class UserCreate(BaseModel):
    user_name: str
    email: str 
    age: int 

# Pydantic のモデル（レスポンス用）
class UserResponse(UserCreate):
    id: int
    created_at: TIMESTAMP

    class Config:
        orm_mode = True
        # TIMESTAMP が pydantic では定義されていないため，下記記述がないとTestUserResponse のcreated_at のvalidation でエラーとなる
        arbitrary_types_allowed = True