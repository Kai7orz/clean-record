from model import create_table 
from models.user import User,UserCreate
from models.record import Record,RecordBase,RecordImageBase
from models.image import Image,ImageCreate 
from models.category import Category,CategoryBase
from models.image import ImageBase,Image
from models.relations import CategoryRecord
from sqlalchemy.orm import Session


# テーブル構築
create_table() 

# # Create 処理群
def insert_user(session:Session,user_name:str,email:str,age:int):
    # User テーブルへのInsert 処理
    users = session.query(User).all()
    # Pydantic オブジェクトでuser 生成
    test_user = UserCreate(user_name=user_name,email=email,age=age)
    # DB に適用するためにSQLAlchemy オブジェクトを Pydanticオブジェクトを基に生成
    db_test_user = User(**test_user.dict())
    # DB へ追加するための処理
    session.add(db_test_user) 
    session.commit()

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


    
def insert_image(session: Session,record_id: int,image_url:str,image_description:str):
    images = session.query(Image).all() 

    test_image = ImageCreate(record_id=record_id,image_url=image_url,image_description=image_description)
    db_test_image = Image(**test_image.dict())

    session.add(db_test_image)
    session.commit()
    
    images = session.query(Image).all() 

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

def get_record_with_image(session: Session, record_id: int):
    # ユーザに対応したimage を取得する
    # クエリ発行
    images = session.query(Image).filter(Image.record_id == record_id).all()
    return images

# category に紐づいたレコードを定義する
def insert_record(session: Session,record_create: RecordBase):
    #insert 時に指定するpydantic の方はinsert 専用のものを指定するのか
    # record 作成して，category.append を入れた後にadd commit 
    record = Record(
        record_name = record_create.record_name
    )
    print("Record_create:",record_create)
    user = session.query(User).filter(User.user_id == record_create.user_id).first()
    print("user found ->",user)
    if(user==None):
        print("user is not found")
    category = session.query(Category).filter(Category.category_id == record_create.category_id ).first()
    record.categories.append(category)
    record.user=user

    print("Insert Record -> user:",user ," category:",category," record:",record)

    session.add(record) 
    session.commit()

def insert_category(session: Session, category_base:CategoryBase):
    category = Category(
        category_name = category_base.category_name
    )
    session.add(category)
    session.commit()

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
    record_with_image = Record(
        record_name = record_with_image_base.record_name,
        user_id =  record_with_image_base.user_id,
    )
    # ここがエラーになるかもしれない
    record_with_image.images = Image(record_id=record_with_image.record_id,image_url=record_with_image_base.image_url,image_description=record_with_image_base.image_description)        
    session.add(record_with_image)
    session.commit()