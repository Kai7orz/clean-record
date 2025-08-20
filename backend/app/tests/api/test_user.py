# TestClient を利用してテストすることが多い
# test したい関数を app から import してくる
# DB をテストケース毎に作成し，unittest を行う
from starlette.testclient import TestClient 
from crud import insert_user 
from main import app 
from db import get_session

def test_insert_user(client):
    resp = client.post(
        "/users/register",
        json={"user_name":"test_user","email":"testuser@example.com","age":"22"},
    )
    assert resp.status_code == 200

# DB から読み込めるかテスト
# DB テストの基準に関する調査