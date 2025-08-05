from crud import get_record_with_image 
from sqlalchemy.orm import Session

def fetch_record_with_image(session: Session,record_id: int) -> dict:
    image_obj = get_record_with_image(session,record_id)
    return image_obj