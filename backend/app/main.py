from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import api.users 
from pydantic import BaseModel 
from typing import Union 
from model import create_table


class Item(BaseModel):
    name: str 
    description: Union[str,None] = None 
    price: float 
    tax: Union[float,None] = None

app = FastAPI() 

origins = [
    "http://localhost:80",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware, 
    allow_origins=origins,
    allow_credentials=True, 
    allow_methods=["*"],
    allow_headers=["*"],
)

#テーブル構築
create_table()

@app.get("/") 
def read_root():
    images = [{"message":"Hello World!"},{"message":"hello image"}]
    return images

app.include_router(api.users.router)
