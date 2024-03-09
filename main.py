import uvicorn
from fastapi import FastAPI

from src.core.config import SETTINGS
import src.api.v1.routes.students as students
import src.api.v1.routes.group as group

app = FastAPI(
    title='fastapi-test-service',
    version=SETTINGS.version,
    docs_url='/api/docs'
)

app.include_router(students.router, prefix='/api/v1', tags=["students"])
app.include_router(group.router, prefix='/api/v1', tags=["groups"])

if __name__ == '__main__':
    uvicorn.run("main:app", host=SETTINGS.host, port=SETTINGS.port)
