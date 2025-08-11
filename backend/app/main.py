from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import api.users 
import api.categories
from pydantic import BaseModel 
from typing import Union 
from model import create_table

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

# Nuxt が起動時にDB 設定のために呼び出す
@app.get("/") 
def read_root():
    #テーブル構築
    create_table()
    completed_message = {"message":"DB setting finished"}
    return completed_message

app.include_router(api.users.router)
app.include_router(api.categories.category_router)