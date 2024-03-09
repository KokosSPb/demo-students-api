from http import HTTPStatus

from fastapi import APIRouter, Depends

from src.api.v1.schema.students import StudentSchema, StudentRequestFilter
from src.core.dependecies.persistance import group_persistence_dependency
from src.domain.group import Group
from src.persistence.base import GroupPersistence

router = APIRouter()


@router.get(
    "/group",
    status_code=HTTPStatus.OK,
    description="Return list of students",
    response_model=list[Group]
)
async def get_groups(
        group_persistence: GroupPersistence = Depends(group_persistence_dependency)
):
    groups = group_persistence.list_groups()
    return groups
