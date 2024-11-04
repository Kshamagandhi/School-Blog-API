# main.py

from fastapi import FastAPI
from routers import blog

app = FastAPI()

app.include_router(blog.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the School Blog API!"}
