import cv2 
import numpy as np

#画像と同サイズのマスクを作成する関数
def make_mask(image_path,output_path="mask.jpg"):
    img = cv2.imread(image_path)
    height, width = img.shape[:2]
    rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    mask = np.zeros(rgb.shape,dtype = np.uint8)
    cv2.rectangle(mask,(0,0),(width,height),(255,255,255),-1)
    cv2.imwrite(output_path,mask)

    return output_path