from sqlalchemy import create_engine 
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker, scoped_session,Session

# 小規模なのでsession は分けずにdb.py に記述
host = "db:3308"
db_name = "sample_db"
user = "mysqluser"
password = "mysqlpass" 

DATABASE = 'mysql://%s:%s@%s/%s?charset=utf8' % (
    user,
    password,
    host,
    db_name,
)

ENGINE = create_engine(
    DATABASE,
    echo=True
)

SessionLocal = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE
        )

Base = declarative_base() 

def get_session() -> Session:
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close() 