from abc import ABC

from src.domain.group import Group


class GroupPersistence(ABC):
    def save(self, name: str, chief: str) -> None:
        ...

    def get_by_id(self, group_id) -> Group:
        ...

    def list_groups(self) -> list[Group]:
        ...