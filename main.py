from fastapi import FastAPI

from db import init_db
from handlers import user_handler

app = FastAPI()

user_router = user_handler.router


@app.on_event("startup")
def on_startup():
    init_db()


@app.get("/ping")
async def pong():
    return {"ping": "pong"}

app.include_router(user_router, prefix="/users")
