# routers/blog.py

from fastapi import APIRouter, HTTPException
from models import BlogPost, BlogPostInDB
from database import blog_posts_collection
from bson import ObjectId

router = APIRouter()

@router.post("/blog/", response_model=BlogPostInDB)
async def create_blog_post(blog_post: BlogPost):
    post_dict = blog_post.dict()
    result = await blog_posts_collection.insert_one(post_dict)
    return {**post_dict, "id": str(result.inserted_id)}

@router.get("/blog/", response_model=list[BlogPostInDB])
async def get_blog_posts():
    posts = []
    async for post in blog_posts_collection.find():
        posts.append(BlogPostInDB(**post, id=str(post["_id"])))
    return posts

@router.get("/blog/{post_id}", response_model=BlogPostInDB)
async def get_blog_post(post_id: str):
    post = await blog_posts_collection.find_one({"_id": ObjectId(post_id)})
    if post is not None:
        return BlogPostInDB(**post, id=str(post["_id"]))
    raise HTTPException(status_code=404, detail="Post not found")

@router.delete("/blog/{post_id}", response_model=dict)
async def delete_blog_post(post_id: str):
    result = await blog_posts_collection.delete_one({"_id": ObjectId(post_id)})
    if result.deleted_count == 1:
        return {"message": "Post deleted"}
    raise HTTPException(status_code=404, detail="Post not found")
