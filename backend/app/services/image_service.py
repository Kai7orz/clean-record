from models.image import ImageBase
from sqlalchemy.orm import Session
from crud import insert_image

def insert_new_image(session: Session,record_id: int,image_url: str,image_description: str = None):
    # DB へのイラストのinsert 
    image_create = ImageBase(
        record_id  = record_id,
        image_url = image_url,
        image_description = image_description 
    )
    insert_image(session=session,image_create=image_create)