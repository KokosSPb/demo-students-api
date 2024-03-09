from src.db.models import GroupModel
from src.domain.group import Group
from src.persistence.base import GroupPersistence
from sqlmodel import Session, select


class PostgresGroupPersistence(GroupPersistence):
    def __init__(self, session: Session):
        self.__session = session

    def save(self, name: str, chief: str) -> None:
        ...

    def get_by_id(self, group_id) -> Group:
        ...

    def list_groups(self) -> list[Group]:
        query = select(GroupModel)
        group_models = self.__session.exec(query).all()
        return [Group(id=group_model.id, name=group_model.name, chief=group_model.chief) for group_model in group_models]