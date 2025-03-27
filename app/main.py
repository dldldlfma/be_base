from fastapi import FastAPI
from app.api.routes import user, login
from fastapi.middleware.cors import CORSMiddleware

CORS_PASS = True

app = FastAPI()

app.include_router(user.router)
app.include_router(login.router)


if CORS_PASS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173"],  # 개발 중이니 정확한 origin을 써
        allow_credentials=True,
        allow_methods=["*"],  # <-- OPTIONS 포함!
        allow_headers=["*"],  # <-- Content-Type, Authorization 포함!
    )


@app.get("/")
async def root():
    return {"message": "Hello, backend base 🏗️"}

