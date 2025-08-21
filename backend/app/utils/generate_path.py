import uuid
# baseURL + UUID のイラストイメージパスの生成
def generate_unique_image_path(filename: str):
    save_url_name = str(uuid.uuid4()) + filename
    return save_url_name