import traceback
from todo_scratch.bk_base.db.db_accesors.base_db_accesor import BaseDbAccesor
from todo_scratch.bk_base.db.entities.entity import Entity
from todo_scratch.bk_base.util.class_loader_util import import_module_member_from_file_route


class QueryDbAccesor(BaseDbAccesor):

    def __init__(self, entity_cls_instance: type) -> None:
        self.entity_cls_instance = entity_cls_instance
        super().__init__()

    def select(self, query: str) -> Entity:
        entity_module: Entity = import_module_member_from_file_route(
            self.entity_cls_instance.__name__,
            self.entity_cls_instance.__module__
        )
        entity = None
        try:
            self.db_driver.connect()
            rows = self.db_driver.query(query)
            entity = entity_module.convert_to_entity(rows[0])
            self.db_driver.disconnect()
        except Exception as e:
            print('error ', e.args)
            print(traceback.format_exc())
            self.db_driver.disconnect()

        return entity
