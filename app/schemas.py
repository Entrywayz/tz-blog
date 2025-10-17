from pydantic import BaseModel

# model
class PostSchema(BaseModel):
    title: str
    content: str