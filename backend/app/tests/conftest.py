import uuid
import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

ADMIN_URL = "mysql+mysqldb://root:rootpass@db:3306/"

def _create_random_db(conn):
    name = f"test_{uuid.uuid4().hex[:8]}"
    conn.execution_options(isolation_level="AUTOCOMMIT").execute(
        text(f"CREATE DATABASE `{name}` CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci")
    )
    return name

def _drop_db(conn, name):
    conn.execution_options(isolation_level="AUTOCOMMIT").execute(
        text(f"DROP DATABASE IF EXISTS `{name}`")
    )

@pytest.fixture(scope="function")
def client():
    # 1) 管理用エンジンで一時DBを作成
    admin = create_engine(ADMIN_URL, pool_pre_ping=True, future=True)
    with admin.connect() as c:
        dbname = _create_random_db(c)

    # 2) 一時DBに接続するエンジン/セッションを用意
    TEST_URL = ADMIN_URL + dbname
    engine = create_engine(TEST_URL, pool_pre_ping=True, future=True)
    SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)

    # 3) app を“ここで”読み込み、依存性を差し替えてから TestClient を作る
    from main import app               # ← 遅延 import（DB作成後）
    from db import Base, get_session   # ← 遅延 import

    # スキーマ作成（Alembic使うなら upgrade head に置換）
    Base.metadata.create_all(engine)

    def override_get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_session] = override_get_db

    from fastapi.testclient import TestClient
    with TestClient(app) as c:
        try:
            yield c
        finally:
            app.dependency_overrides.clear()

    engine.dispose()
    with admin.connect() as c:
        _drop_db(c, dbname)
    admin.dispose()
