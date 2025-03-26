from fastapi import FastAPI
from app.api.routes import user

app = FastAPI()

app.include_router(user.router)

@app.get("/")
async def root():
    return {"message": "Hello, backend base 🏗️"}
