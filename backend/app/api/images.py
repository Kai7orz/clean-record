from fastapi import APIRouter ,Depends
from pydantic import BaseModel 
from db import get_session 
from sqlalchemy.orm import Session
from services.image_service import insert_new_image

class ImageInfo(BaseModel):
    record_id: int
    image_url: str
    image_description: str

image_router = APIRouter()

@image_router.post("/images")
async def create_new_image(image_info:ImageInfo,session:Session=Depends(get_session)):
    insert_new_image(session=session,record_id=image_info.record_id,image_url=image_info.image_url,image_description=image_info.image_description)

