from model import create_table 
from models.user import Users,UserCreate
from models.record import Records,RecordCreate 
from models.image import Images,ImageCreate 
from models.category import Categories,CategoryCreate
from sqlalchemy.orm import Session

# テーブル構築
create_table() 

# # Create 処理群
# def InsertUser():
#     # User テーブルへのInsert 処理
#     users = session.query(Users).all()
#     print("Users Before Inserting:",users)
#     # Pydantic オブジェクトでuser 生成
#     test_user = UserCreate(user_name="name_test",email="name@example.com",age=10)
#     # DB に適用するためにSQLAlchemy オブジェクトを Pydanticオブジェクトを基に生成
#     db_test_user = Users(**test_user.dict())
#     # DB へ追加するための処理
#     session.add(db_test_user) 
#     session.commit()

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

# def InsertRecord():
#     records = session.query(Records).all() 
#     print("Records Before Inserting:",records)
#     test_record = RecordCreate(record_name="test用のレコード")
#     db_test_record = Records(**test_record.dict())

#     session.add(db_test_record) 
#     session.commit() 

#     records = session.query(Records).all() 

#     print("Records After Inserting:",records)
    
# def InsertImage():
#     images = session.query(Images).all() 
#     print("Images Before Inserting:",images) 
    
#     test_image = ImageCreate(record_id=1,image_url="https://fjibxkzzwqkhzotywbdh.supabase.co/storage/v1/object/public/clean-up-bucket//illust.png",image_description="test description of image")
#     db_test_image = Images(**test_image.dict())

#     session.add(db_test_image)
#     session.commit()
    
#     images = session.query(Images).all() 
#     print("Images After Inserting:",images)

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
    images = session.query(Images).filter(Images.record_id == record_id).all()
    return images