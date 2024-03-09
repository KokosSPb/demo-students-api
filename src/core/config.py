from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    debug: bool
    host: str
    port: int
    version: str

    db_name: str
    db_hostname: str
    db_port: int
    db_user: str
    db_password: str

    secret_key: str


SETTINGS = Settings()
