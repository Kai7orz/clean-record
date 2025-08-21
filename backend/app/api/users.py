from fastapi import APIRouter,Depends
import cv2 
import io
import os 
from fastapi import UploadFile
# from crud import InsertUser,ge,InsertCategory,InsertRecord,ReadRecord,ReadCategory,ReadImage
# from crud import UpdateRecord
import sys 
from utils.resize_image import resize_image
from utils.make_mask import make_mask
from utils.convert_rgb_to_rgba import convert_to_rgba_image
from utils.upload_illustration import upload_illustration
from services.gpt_image_client import call_gpt_with_image
from services.user_service import register_user,fetch_record_with_image,create_record
from db import get_session
from pydantic import BaseModel 
from sqlalchemy.orm import Session

class RegisterInfo(BaseModel):
    user_name: str 
    email: str 
    age: str

class RecordInfo(BaseModel):
    user_id: int 
    category_id: int
    record_name: str


router = APIRouter() 

@router.get("/users/{user_id}")
async def read_user(user_id: int, session: Session=Depends(get_session)):
    print("User :",user_id)
    print("record 1 :")
    record_id = 2
    image_obj = fetch_record_with_image(session,record_id=record_id)
    print("Image Object: ",image_obj)
    return image_obj

@router.post("/users/{user_id}/")
async def get_illustration(ufile: UploadFile):
    bf = await ufile.read()
    if not bf:
        print("file is empty",flush=True)
    os.makedirs("./assets/images",exist_ok = True)
    path = f'./assets/images/{ufile.filename}'
    with open(path,'wb') as buffer:
        buffer.write(bf)

    image_path = path 
    resized_image_path = resize_image(image_path)
#    converted_image_path = convert_to_rgba_image(resized_image_path,mask=False)
    custom_output_path = "assets/images/mask.png" 
    #RGB 形式のMask 画像のパス
    mask_raw_output_path = make_mask(image_path=resized_image_path,output_path=custom_output_path)
    #RGBA 形式変換後の画像のパス
    converted_mask_path=convert_to_rgba_image(mask_raw_output_path,mask=True)
    #call_gpt_with_image(converted_image_path,converted_mask_path)
    # 個のレスポンスを待ってから 下の処理に進んでいるか確認する必要がありそう
    image_path = "assets/images/illust.png"
    im = cv2.imread(image_path) 
    byte_image,buf = cv2.imencode(".png",im) 

    uploaded_image_path = upload_illustration(image_path)

    print("image->",uploaded_image_path)
    return {"image_url": uploaded_image_path}

@router.post("/users/register")
async def register_new_user(register_info:RegisterInfo,session: Session=Depends(get_session)):
    print("登録情報の読み取り... name:",register_info.user_name," email:",register_info.email," age:",register_info.age)
    register_user(session=session,user_name=register_info.user_name,email=register_info.email,age_string=register_info.age)

@router.post("/users/{user_id}/records")
async def create_new_record(record_info:RecordInfo,session: Session=Depends(get_session)):
    print(record_info)
    create_record(session=session,user_id=record_info.user_id,category_id=record_info.category_id,record_name=record_info.record_name)
