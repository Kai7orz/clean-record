from fastapi import APIRouter,Depends
from fastapi import UploadFile
# from crud import InsertUser,ge,InsertCategory,InsertRecord,ReadRecord,ReadCategory,ReadImage
# from crud import UpdateRecord
import sys 
from services.user_service import create_record_with_image,upload_image,register_user,fetch_record_with_image,create_record
from db import get_session
from schemas.user import UserRegisterInfo 
from pydantic import BaseModel 
from sqlalchemy.orm import Session

class RecordInfo(BaseModel):
    user_id: int 
    category_id: int
    record_name: str

class RecordImageInfo(BaseModel):
    #autoincrement を利用するのでrecord_id は指定しない
    user_id: int 
    category_id: int 
    record_name: str 
    image_url: str 
    image_description: str

router = APIRouter() 

@router.get("/users/{user_id}")
async def read_user(user_id: int, session: Session=Depends(get_session)):
    # パスパラメータとして読み込む
    image_obj = fetch_record_with_image(session,user_id=user_id)
    print("Image Object: ",image_obj)
    return image_obj

@router.post("/users/{user_id}/")
async def get_illustration(ufile: UploadFile,session: Session=Depends(get_session)):
    uploaded_image_path = await upload_image(uploaded_file=ufile)
    print("image->",uploaded_image_path)
    return {"image_url": uploaded_image_path}
# test 実装済み
@router.post("/users/register")
async def register_new_user(register_info:UserRegisterInfo,session: Session=Depends(get_session)):
    register_user(session=session,user_name=register_info.user_name,email=register_info.email,age=register_info.age)

@router.post("/users/{user_id}/records")
async def create_new_record(record_info:RecordInfo,session: Session=Depends(get_session)):
    create_record(session=session,user_id=record_info.user_id,category_id=record_info.category_id,record_name=record_info.record_name)

@router.post("/users/{user_id}/records/images")
async def create_new_record_with_image(record_image_info:RecordImageInfo,session: Session=Depends(get_session)):
    create_record_with_image(
                             session=session,
                             user_id=record_image_info.user_id,
                             category_id=record_image_info.category_id,
                             record_name=record_image_info.record_name,
                             image_url=record_image_info.image_url,
                             image_description=record_image_info.image_description
    )