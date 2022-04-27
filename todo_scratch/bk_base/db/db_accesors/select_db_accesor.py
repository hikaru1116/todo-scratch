import traceback
from typing import Dict, List
from todo_scratch.bk_base.db.db_accesors.base_db_accesor import BaseDbAccesor
from todo_scratch.bk_base.db.entities.entity import Entity


class SelectDbAccesor(BaseDbAccesor):

    def select(self, query: str, param: Dict = {}) -> List[Entity]:
        entities: List = []
        try:
            self.db_driver.connect()
            rows: Dict = self.db_driver.query(query)
            entities = self.entity_service.create_entity_list(rows)
            self.db_driver.disconnect()
        except BaseException:
            self.db_driver.disconnect()
            print(traceback.format_exc())
        return entities
