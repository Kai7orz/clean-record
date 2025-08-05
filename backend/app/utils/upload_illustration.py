import os 
from dotenv import load_dotenv
from supabase import create_client 

def upload_illustration(filepath: str,bucket: str = "clean-up-bucket") -> str:

    load_dotenv()
    SUPABASE_URL = os.environ['SUPABASE_URL']
    SUPABASE_KEY = os.environ['SUPABASE_KEY']
    supabase = create_client(SUPABASE_URL,SUPABASE_KEY)

    filename = os.path.basename(filepath)
    
    if not os.path.exists(filepath):
        raise FileNotFoundError("file not found")
    
    with open(filepath,"rb") as f:
        supabase.storage.from_(bucket).upload(filename,f,file_options={"content-type":"img/png","upsert":"true"})
    public_url = f"{SUPABASE_URL}/storage/v1/object/public/{bucket}/{filename}" 
    print("ok✅:",public_url)
    return public_url
