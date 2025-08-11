from fastapi import APIRouter ,Depends
from pydantic import BaseModel 
from db import get_session 
from sqlalchemy.orm import Session
from image_service import create_image


class ImageInfo(BaseModel):
    image_url: str
    image_description: str

image_router = APIRouter()

@image_router.post("/images")
async def create_new_image(image_info:ImageInfo,session:Session=Depends(get_session)):
    create_image(session=session)