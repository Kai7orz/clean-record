# TestClient を利用してテストすることが多い
# test したい関数を app から import してくる
# DB をテストケース毎に作成し，unittest を行う
from starlette.testclient import TestClient 
from crud import insert_user 
from main import app 
from db import get_session

# 必要な DB を一時的に作成し利用できるようにするデコレ―タ
def temp_db(f):
    def func(SessionLocal, *args, **kwargs):
        def override_get_db():
            try:
                db = SessionLocal()
                yield db 
            finally:
                db.close()

        app.dependency_overrides[get_session] = override_get_db
    return func

client = TestClient(app)

@temp_db
def test_insert_user():
    response = client.post(
        "/users/register", json={"user_name":"test_user","email":"testuser@example.com","age":"22"}
    )
    assert response.status_code == 200 
