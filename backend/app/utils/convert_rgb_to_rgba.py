from pathlib import Path
from PIL import Image

# rgb のイメージを受け取って，rgba 形式の画像にコンバートしたパスを返す
# mask なら true を引数に受け取って，透明度0に指定
# 元のモデル画像なら mask false を受け取って透明度255に指定
def convert_to_rgba_image(rgb_image_path,mask):

    converted_image_path=""
    img_obj = Image.open(rgb_image_path).convert("RGBA")
    if mask:
        img_obj.putalpha(alpha=0)
        mask_output_path = Path(__file__).resolve().parent.parent / "assets" / "images" / "mask.png"
        converted_image_path = mask_output_path
    else:
        img_obj.putalpha(alpha=255)
        original_output_path = Path(__file__).resolve().parent.parent / "assets" / "images" / "original_image.png"
        converted_image_path = original_output_path
    img_obj.save(converted_image_path)

    return converted_image_path
