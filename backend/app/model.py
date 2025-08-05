from typing import Optional
from sqlalchemy import ForeignKey,Column,Integer,String,TIMESTAMP,PrimaryKeyConstraint
from sqlalchemy.orm import relationship 
from sqlalchemy.schema import FetchedValue
from pydantic import BaseModel 
from db import Base 
from db import ENGINE 

# 規模小さいので　すべて model.py にまとめて記述する

def create_table():
    Base.metadata.create_all(bind=ENGINE)
    # models で定義したBase 継承したクラスのテーブル全てcreate させたい
    # そのためにはcreate_all の挙動について知る必要がある（何を知るべきかについて常に意識しておく）
    # Base が継承されているクラスについてすべてテーブルが自動作成されるか否かを見たい
    # テーブルはBase を継承したクラスで定義する
        # 他のファイルに記述したBase 継承クラスを認識させる必要があるか？あればどのように認識させるのかがわからない