from pydantic import BaseModel

class UserRegisterInfo(BaseModel):
    user_name: str 
    email: str 
    age: str