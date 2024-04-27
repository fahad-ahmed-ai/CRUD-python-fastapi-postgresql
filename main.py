from fastapi import FastAPI
import uvicorn as uvicorn
from Utilities.init_db import init_db
import asyncio
from fastapi.middleware.cors import CORSMiddleware
from crud_app.routers import router

app = FastAPI(title="APIs Docs")
app.include_router(router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "main":
    init_db()
