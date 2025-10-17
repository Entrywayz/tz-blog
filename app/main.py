from fastapi import FastAPI, HTTPException
from database import SessionLocal, engine, Base
from schemas import PostSchema
from models import Post

app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.get("/posts")
def get_posts():
    db = SessionLocal()
    posts = db.query(Post).all()
    db.close()
    return posts

@app.post("/posts")
def create_post(post: PostSchema):
    db = SessionLocal()
    new_post = Post(title=post.title, content=post.content)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    db.close()
    return new_post