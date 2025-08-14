import os 
import cv2 
import shutil
from models.record import RecordBase,RecordImageBase
from models.image import ImageBase
from crud import get_record_with_image,insert_user,insert_image,insert_record,insert_record_with_image
from sqlalchemy.orm import Session
from fastapi import UploadFile
from utils.resize_image import resize_image
from utils.make_mask import make_mask
from utils.convert_rgb_to_rgba import convert_to_rgba_image
from services.clients.upload_illustration import upload_illustration
from services.clients.gpt_image_client import call_gpt_with_image

# このサービス層（ビジネスロジック）では，session 層に対して，pydantic のオブジェクトに包んでデータを渡す
# SQLAlchemy のオブジェクトに展開するのは session 層の責務とする

def fetch_user_with_image(session: Session,user_id: int) -> dict:
    pass 

def register_user(session: Session,user_name:str,email:str,age:int) -> dict:
    # user register validation を記述する必要がある
    insert_user(session=session,user_name=user_name,email=email,age=age)

def create_record(session: Session,user_id:int,category_id:int,record_name:str):
    record_create = RecordBase(
        record_name = record_name,
        user_id = user_id ,
        category_id = category_id ,
    )
    insert_record(session=session,record_create=record_create)

def create_record_with_image(session: Session,user_id:int,category_id:int,record_name:str,image_url:str,image_description:str=None):
    record_with_image_create = RecordImageBase(
        user_id=user_id, 
        category_id=category_id,
        record_name=record_name,
        image_url=image_url,
        image_description=image_description
    )
    insert_record_with_image(session=session,record_with_image_base=record_with_image_create)


def fetch_record_with_image(session: Session,record_id: int) -> dict:
    image_url = "https://fjibxkzzwqkhzotywbdh.supabase.co/storage/v1/object/public/clean-up-bucket//illust.png"
    image_description = "test description of image"
    image_obj = get_record_with_image(session,record_id)
    return image_obj

def upload_image(uploaded_file): 
    bf = uploaded_file.read()
    if not bf:
        print("file is empty",flush=True)
    os.makedirs("./assets/images",exist_ok = True)
    path = f'./assets/images/{uploaded_file.filename}'
    with open(path,'wb') as buffer:
        shutil.copyfileobj(uploaded_file.file, buffer)

    image_path = path 
    resized_image_path = resize_image(image_path)
    converted_image_path = convert_to_rgba_image(resized_image_path,mask=False)
    custom_output_path = "assets/images/mask.png" 
    #RGB 形式のMask 画像のパス
    mask_raw_output_path = make_mask(image_path=resized_image_path,output_path=custom_output_path)
    #RGBA 形式変換後の画像のパス
    converted_mask_path=convert_to_rgba_image(mask_raw_output_path,mask=True)
    call_gpt_with_image(converted_image_path,converted_mask_path)
    # 個のレスポンスを待ってから 下の処理に進んでいるか確認する必要がありそう
    image_path = "assets/images/illust.png"
    # メモリーのread
    im = cv2.imread(image_path) 
    byte_image,buf = cv2.imencode(".png",im) 
    # 指定したurl の画像をsupabase へアップロードする
    uploaded_image_path = upload_illustration(image_path)

    return uploaded_image_path
    