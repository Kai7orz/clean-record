from models.record import RecordBase 
from crud import get_record_with_image,insert_user,insert_image,insert_record
from sqlalchemy.orm import Session

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

def fetch_record_with_image(session: Session,record_id: int) -> dict:
    image_url = "https://fjibxkzzwqkhzotywbdh.supabase.co/storage/v1/object/public/clean-up-bucket//illust.png"
    image_description = "test description of image"
    image_obj = get_record_with_image(session,record_id)
    return image_obj
