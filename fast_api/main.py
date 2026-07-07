
# uvicorn main:app --reload [to start server]

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message":"hello world"}