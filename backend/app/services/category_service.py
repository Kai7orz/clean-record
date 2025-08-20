from sqlalchemy.orm import Session
from models.category import CategoryBase
from crud import insert_category

def create_category(session: Session,category_name: str):
    category_base = CategoryBase(
        category_name = category_name
    )
    
    insert_category(session=session,category_base=category_base)