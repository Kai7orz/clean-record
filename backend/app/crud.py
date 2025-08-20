from pydantic import ValidationError
from fastapi import FastAPI, HTTPException
from models.user import User,UserCreate
from models.record import Record,RecordBase,RecordImageBase
from models.image import Image,ImageBase
from models.category import Category,CategoryBase
from models.image import ImageBase,Image
from models.relations import CategoryRecord
from typing import List
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import IntegrityError,SQLAlchemyError



# # Create 処理群
def insert_user(session:Session,user_name:str,email:str,age:int):
    try:
        # Pydantic オブジェクトでuser 生成
        new_user = UserCreate(user_name=user_name,email=email,age=age)
        # DB に適用するためにSQLAlchemy オブジェクトを Pydanticオブジェクトを基に生成
        db_new_user = User(**new_user.dict())
        # DB へ追加するための処理
    except ValidationError as ve:
        raise HTTPException(status_code=422,detail=ve.errors())
    try:
        session.add(db_new_user) 
        session.commit()
    
    except IntegrityError as e:
        session.rollback()
        raise HTTPException(
            status_code = 409,
            detail={"code":"user insert error","message":"不正なユーザーのinsert error"}
        )
    except SQLAlchemyError as e:
        session.rollback()
        raise HTTPException(
            status_code=500,
            detail={"code":"db_error","message":"データベースエラーが発生"}
        )


#     users = session.query(Users).all()
#     print("Users After Inserting:",users)

# def InsertCategory():
#     categories = session.query(Categories).all() 
#     print("Categories Before Inserting:",categories)

#     test_category = CategoryCreate(category_name="test_category")
#     db_test_category = Categories(**test_category.dict())

#     session.add(db_test_category)
#     session.commit() 

#     categories = session.query(Categories).all()

#     print("Categories After Inserting:",categories)

# def insert_record(session:Session,user_id:int,category_id:int,record_name:str):

#     #user　で User 情報取得する必要があるかも

#     user = session.query(Users).filter(Users.user_id == user_id).first()
    
#     test_record = RecordCreate(record_name=record_name)
#     db_test_record = Records(
#             **test_record.dict(),
#             user_id = user.user_id,
#             category_id = category_id,
#                              )

#     session.add(db_test_record) 
#     session.commit() 

# # Read 処理群

# def ReadRecord():
#     records = session.query(Records).all() 
#     # records
#     for record in records:
#         print("ReadRecord✅:",record)
#         print("👀 Record_name:",record.record_name)

# def ReadImage():
#     images = session.query(Images).all()
#     for image in images:
#         print("image:",image)

# def ReadCategory():
#     categories = session.query(Categories).all() 
#     for category in categories:
#         print("category:",category)


# def ReadRecordWithImage():
#     images = session.query(Images).all()    
#     for img in images:
#         print("img からレコードをたどってみる -> ",img.record.record_id)

# # Update 処理群

# def UpdateRecord():
#     target_id = 1 
#     target_record = session.query(Records).filter(Records.record_id==target_id).first()
#     target_record.record_name = "新しくレコードの名前を編集した"
#     session.commit()
#     print("✅レコード更新")
# # Delete 処理群

# def DeleteRecord():
#     target_id = 1 
#     target_record = session.query(Records).filter(Records.record_id==target_id).first() 
#     session.delete(target_record)
#     session.commit()
#     print("✅レコード削除")

def get_record_with_image(session: Session, user_id: int):
    # ユーザに対応したimage を取得する
    # クエリ発行
    stmt = (
        select(Image)
        .join(Image.record)
        .where(Record.user_id == user_id)
        .order_by(Image.image_id.desc())
    )
    images = session.execute(stmt).scalars().all()
    return images

# user・category に紐づいたレコードを定義する
def insert_record(session: Session,record_create: RecordBase):
    #insert 時に指定するpydantic の方はinsert 専用のものを指定するのか
    # record 作成して，category.append を入れた後にadd commit 
    record = Record(
        record_name = record_create.record_name
    )
    user = session.query(User).filter(User.user_id == record_create.user_id).first()
    if(user==None):
        raise HTTPException(
            status_code = 404,
            detail={"code":"user not found","message":"指定したユーザーが見つかりませんでした"}
        )

    category = session.query(Category).filter(Category.category_id == record_create.category_id ).first()
    if(category == None):
        raise HTTPException(
            status_code = 404,
            detail={"code":"category not found","message":"指定したカテゴリーが見つかりませんでした"}
        )
    try:
        record.categories.append(category)
        record.user=user

        session.add(record) 
        session.commit()

    except IntegrityError as e:
        session.rollback()
        raise HTTPException(
            status_code = 404,
            detail={"code": "DB insert error","message":"DB でエラー"}
    )

    except Exception:
        session.rollback() 
        raise HTTPException(
            status_code = 404,
            detail={"code":"INTERNAL ERROR","message":"サーバー内部でのエラー"}
        ) 
    
def insert_category(session: Session, category_base:CategoryBase):
    try:
        category = Category(
            category_name = category_base.category_name
        )
        session.add(category)
        session.commit()
    
    except IntegrityError as e:
        raise HTTPException(
            status_code = 400,
            detail={"code":"Bad_request","message":"不正な入力"}
        )

# 中間テーブルは。レコード挿入時に介入・カテゴリーインサートには関与しないという理解

def insert_image(session: Session,image_base:ImageBase):
    image = Image(
        record_id = image_base.record_id,
        image_url = image_base.image_url,
        image_description = image_base.image_description
    )
    session.add(image)
    session.commit()

def insert_record_with_image(session: Session,record_with_image_base:RecordImageBase):

    user = session.get(User,record_with_image_base.user_id)
    if user is None:    
        raise HTTPException(
            status_code = 404,
            detail={"code":"user not found","message":"指定したユーザーが見つかりませんでした"}
        )
    
    record_with_image = Record(
        record_name = record_with_image_base.record_name,
        user_id =  record_with_image_base.user_id,
    )
    try:
        session.add(record_with_image)
        session.flush()
        image = Image(record_id=record_with_image.record_id,image_url=record_with_image_base.image_url,image_description=record_with_image_base.image_description)

        session.add(image)
        session.commit()
    except:
        session.rollback() 
        raise HTTPException(
            status_code = 404,
            detail={"code":"DB insert error","message":"DB にデータ挿入時エラーが発生しました"}
        )
    finally:
        session.close()