from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import search

app = FastAPI(title="ATD Music Search API")

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root() -> str:
    return "Welcome to ATD Music Search API!"


app.include_router(search.router)
