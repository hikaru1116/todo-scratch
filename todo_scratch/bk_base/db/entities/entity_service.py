from typing import Dict, List
from todo_scratch.bk_base.db.entities.entity import Entity

from todo_scratch.bk_base.util.class_loader_util import import_module_member_from_file_route


class EntityService:

    def __init__(self, entity_module: type) -> None:
        self.entity_module: type = entity_module

    def create_entity_list(self, rows: List[Dict]) -> List:
        entities = []
        for row in rows:
            entity_module: type = import_module_member_from_file_route(
                self.entity_module.__name__,
                self.entity_module.__module__
            )
            entity: Entity = entity_module()
            entity.set_values_by_row(row)
            entities.append(entity)
        return entities
