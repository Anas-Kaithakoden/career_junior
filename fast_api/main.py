
# uvicorn main:app --reload [to start server]

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message":"hello world"}

@app.get("/postss")
def list_posts():
    return [
        {
            "id": 1,
            "title": "FastAPI Basics"
        },
        {
            "id": 2,
            "title": "SQLAlchemy"
        }
    ]

@app.get("/postsss/{post_id}")
def return_posts(post_id : int):
    return {
        "post_id" : 5
    }

@app.get("/postssss?limit=10")
def send_posts(limit: int = 10):
    return {
    "limit": 10
}


# pydantic, validation

from typing import Optional
from pydantic import BaseModel, Field

class PostCreate(BaseModel): # Request model
    title: str = Field(min_length=3, max_length=100)
    content: str = Field(min_length=10)
    published: bool = False
    summary: Optional[str] = None


@app.post("/posts")
def create_post(post: PostCreate):
    return {
        "title": post.title,
        "content": post.content
    }

# Response Models

class UserResponse(BaseModel):
    id: int
    username: str
    email: str

@app.get("/users/{id}", response_model=UserResponse)
def get_user(id: int):
    ...


# Exercise:

class PostCreateEX(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    content: str = Field(min_length=10)
    summary: Optional[str] = None
    published: bool = False

@app.post("/postsEX")
def create_posts(post: PostCreateEX):
    return {
        "title": post.title,
        "content": post.content,
        "published" : post.published,
        "message": "Hi"
    }


# Depends

# def get_db():
#     with SessionLocal() as session:
#         yield session

# def get_db():
#     db = SessionLocal()

#     try:
#         yield db

#     finally:
#         db.close()