# database.py

from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient
import os

MONGO_DETAILS = os.getenv("MONGO_DETAILS", "mongodb+srv://school_blog:drymanchurian1109@cluster0.lfth5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.school_blog  # Replace with your database name
blog_posts_collection = database.blog_posts  # Replace with your collection name