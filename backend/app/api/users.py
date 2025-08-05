from fastapi import APIRouter,Depends
import cv2 
import io
import os 
from fastapi import UploadFile
# from crud import InsertUser,InsertImage,InsertCategory,InsertRecord,ReadRecord,ReadCategory,ReadImage
# from crud import UpdateRecord
import sys 
from utils.resize_image import resize_image
from utils.make_mask import make_mask
from utils.convert_rgb_to_rgba import convert_to_rgba_image
from utils.upload_illustration import upload_illustration
from services.gpt_image_client import call_gpt_with_image
from services.user_service import fetch_record_with_image
from db import get_session
from sqlalchemy.orm import Session
router = APIRouter() 

@router.get("/users/{user_id}")
async def read_user(user_id: int, session: Session=Depends(get_session)):
    print("User :",user_id)
    print("record 1 :")
    record_id = 1
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

