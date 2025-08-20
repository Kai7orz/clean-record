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

@app.on_event("startup")
def on_startup():
    create_table()

app.include_router(api.users.router)
app.include_router(api.categories.category_router)