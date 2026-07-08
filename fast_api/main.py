
# uvicorn main:app --reload [to start server]

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message":"hello world"}

@app.get("/posts")
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

@app.get("/posts/{post_id}")
def return_posts(post_id : int):
    return {
        "post_id" : 5
    }

@app.get("/posts?limit=10")
def send_posts(limit: int = 10):
    return {
    "limit": 10
}