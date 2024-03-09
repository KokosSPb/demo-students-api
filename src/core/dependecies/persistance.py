from fastapi import Depends
from sqlmodel import Session

from src.core.db_config import DB_ENGINE
from src.persistence.base import GroupPersistence
from src.persistence.postgres import PostgresGroupPersistence


def session_dependency():
    with Session(DB_ENGINE) as session:
        yield session


def group_persistence_dependency(session: Session = Depends(session_dependency)) -> GroupPersistence:
    return PostgresGroupPersistence(session)
