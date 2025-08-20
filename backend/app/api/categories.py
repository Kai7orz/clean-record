from fastapi import APIRouter,Depends
from pydantic import BaseModel 
from db import get_session 
from sqlalchemy.orm import Session
from services.category_service import create_category

class CategoryInfo(BaseModel):
    category_name: str 

category_router = APIRouter()

@category_router.post("/categories")
async def create_new_category(category_info:CategoryInfo ,session: Session=Depends(get_session)):
    create_category(session=session,category_name = category_info.category_name)