from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query

from src.database.database import create_db_and_tables
from src.database.models.hero import Hero

from src.routes.heroes import router as register_heroes_routes

app = FastAPI()

register_heroes_routes(app)

@app.on_event("startup")
async def on_startup():
    create_db_and_tables()
