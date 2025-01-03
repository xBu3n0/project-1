from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query

# Import all the models
import src.database.models.hero

from sqlmodel import Field, Session, SQLModel
from sqlmodel import create_engine, select

# from os import environ as env
# postgres_url = f"postgresql://{env['DB_USERNAME']}:{env['DB_PASSWORD']}@{env['DB_ROUTE']}/{env['DATABASE']}?schema=public"

# The sqlite will be changed to PostgreSQL
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}

engine = create_engine(sqlite_url, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]
