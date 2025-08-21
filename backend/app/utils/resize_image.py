import cv2
from pathlib import Path 

async def resize_image(image_path):
    try:
        width_size = 1024 
        height_size = 1024

        if Path(image_path).exists():
            print("✅ image 存在する")
            img = cv2.imread(image_path)
        else:
            print("image_path:",image_path)
            print("パスが存在しない✖")
        resized_img = cv2.resize(img,(width_size,height_size))
        output_path = Path(__file__).resolve().parent.parent / "assets" / "images" / "input_resized_image.png"
        cv2.imwrite(output_path,resized_img)
        return output_path
    except Exception as e:
        print(e,flush=True) 
        return None
