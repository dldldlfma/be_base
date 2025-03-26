from typing import Union
from fastapi import FastAPI
from app.core.config import settings

app = FastAPI()


@app.get("/")
def read_root():
    return {"db_url": settings.database_url}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}