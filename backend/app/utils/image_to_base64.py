import base64 

#入力：encode する画像のパス
#出力：encode 済の画像オブジェクト
def image_to_base64(raw_image_path):
    with open(raw_image_path,'rb') as f:
            data = f.read()
    encode=base64.b64encode(data)
    # str としてbase64 のデータを返す
    return encode


