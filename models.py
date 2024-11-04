# models.py

from pydantic import BaseModel
from typing import Optional
from bson import ObjectId

class BlogPost(BaseModel):
    title: str
    content: str
    author: str

class BlogPostInDB(BlogPost):
    id: str

    class Config:
        orm_mode = True
