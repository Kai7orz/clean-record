import base64
import sys 
from openai import OpenAI 
from pathlib import Path 
parent_path=Path(__file__).resolve().parent
sys.path.append(str(parent_path))
from utils.make_mask import make_mask
from utils.image_to_base64 import image_to_base64
from utils.convert_rgb_to_rgba import convert_to_rgba_image

# 引数:image のpath 
# 出力:GPT API からのレスポンスイラストオブジェクト
def call_gpt_with_image(resized_image_path,mask_image_path):
    try:
        client = OpenAI()
        # base64_image = image_to_base64(image_path)
        prompt =   "画像をイラスト化して"
        model = "gpt-image-1"
        output_path = Path(__file__).resolve().parent.parent.parent / "assets" / "images" / "illust.png"

        with open(resized_image_path,"rb") as image_file,open(mask_image_path,"rb") as mask_file:
            result = client.images.edit(
                model=model,
                quality="low",
                image=image_file,
                prompt=prompt
            )

            print("API Result -> ",result,flush=True)

            response_image_base64 = result.data[0].b64_json 
            image_bytes = base64.b64decode(response_image_base64)

            with open(output_path,"wb") as f:
                f.write(image_bytes)

    # openAI からのレスポンスはローカルに保存されないので，web 上でファイルをオープンしてローカルに書き込む処理を入れておく
    except FileNotFoundError as e:
        print("File Not Found ",e)
        raise

    except base64.binascii.Error as e:
        print("Base64 Decode Error ",e)
        raise

    except Exception as e:
        print("Error :",e)
        raise
