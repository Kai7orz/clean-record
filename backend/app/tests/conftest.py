import pytest
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, drop_database 
from db import Base 

@pytest.fixture(scope="function")
def SessionLocal():
    host = "db"
    db_name = "test_db"
    user = "testuser"
    password = "testpass" 
    port = "3306"

    TEST_DATABASE =  "mysql+mysqldb://{}:{}@{}:{}/{}".format(
            user,
            password,   
            host,
            port,
            db_name,
        )

    ENGINE = create_engine(
        TEST_DATABASE,
        echo=True
    )

    engine = create_engine(TEST_DATABASE)

    assert not database_exists(TEST_DATABASE),"Test DB already exists."

    Base.metadata.create_all(engine) 
    SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=ENGINE)

    yield SessionLocal 

    drop_database(TEST_DATABASE)