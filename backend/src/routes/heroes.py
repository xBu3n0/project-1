from src.database.models.hero import Hero

from typing import Annotated

from fastapi import Query
from src.database.database import create_db_and_tables, SessionDep, select

def router(app):
  @app.post("/heroes/")
  async def create_hero(hero: Hero, session: SessionDep) -> Hero:
      session.add(hero)
      session.commit()
      session.refresh(hero)
      return hero

  @app.get("/heroes/")
  async def read_heroes(
      session: SessionDep,
      offset: int = 0,
      limit: Annotated[int, Query(le=100)] = 100,
  ) -> list[Hero]:
      heroes = session.exec(select(Hero).offset(offset).limit(limit)).all()
      return heroes
