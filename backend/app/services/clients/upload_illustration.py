import uuid 
import os 
from utils.generate_path import generate_unique_image_path
from dotenv import load_dotenv
from supabase import create_client 


def upload_illustration(filepath: str,bucket: str = "clean-up-bucket") -> str:
    # イラスト化した画像のurl path を返す
    load_dotenv()
    SUPABASE_URL = os.environ['SUPABASE_URL']
    SUPABASE_KEY = os.environ['SUPABASE_KEY']
    supabase = create_client(SUPABASE_URL,SUPABASE_KEY)

    save_url_name = ""
    filepath = filepath
    filename = os.path.basename(filepath)
    
    if not os.path.exists(filepath):
        raise FileNotFoundError("file not found")
    
    with open(filepath,"rb") as f:
        save_url_name = generate_unique_image_path(filename)
        supabase.storage.from_(bucket).upload(save_url_name,f,file_options={"content-type":"img/png","upsert":"true"})
    # baseURL
    public_url = f"{SUPABASE_URL}/storage/v1/object/public/{bucket}/{save_url_name}" 
    print("ok✅:",public_url)
    return public_url
