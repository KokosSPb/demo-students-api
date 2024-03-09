from pydantic import PostgresDsn
from sqlmodel import create_engine, Session

from src.core.config import SETTINGS

DB_URI = PostgresDsn.build(
    scheme='postgresql',
    user=SETTINGS.db_user,
    password=SETTINGS.db_password,
    host=f"{SETTINGS.db_hostname}:{SETTINGS.db_port}",
    path=f"/{SETTINGS.db_name}"
)

DB_ENGINE = create_engine(DB_URI)

SESSION = Session(DB_ENGINE)