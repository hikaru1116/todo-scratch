import logging
import traceback
from typing import Dict, List
from todo_scratch.bk_base.db.db_accesors.base_db_accesor import BaseDbAccesor
from todo_scratch.bk_base.db.db_accesors.query_factory import QueryFactory
from todo_scratch.bk_base.db.entities.entity import Entity
from todo_scratch.bk_base.util.log.log_util import get_main_logger


class DbAccesor(BaseDbAccesor):

    def __init__(self, entity_type: type) -> None:
        self.logger: logging.Logger = get_main_logger()
        self.query_factory = QueryFactory()
        super().__init__(entity_type)

    def select(self,) -> List[Entity]:
        entities: List[Entity] = []
        try:
            self.db_driver.connect()
            query = self.query_factory.create_select_query(self.entity_type())
            rows = self.db_driver.fetch_with_param(query, ())
            entities = self.entity_service.create_entity_list(rows)
        except Exception:
            self.logger.error(traceback.format_exc())
        finally:
            self.db_driver.disconnect()
        return entities

    def select_by_id(self, id) -> Entity:
        entities: List[Entity] = []
        try:
            self.db_driver.connect()
            query = self.query_factory.create_select_query_by_id(self.entity_type())
            rows = self.db_driver.fetch_with_param(query, (id,))
            entities = self.entity_service.create_entity_list(rows)
        except Exception:
            self.logger.error(traceback.format_exc())
        finally:
            self.db_driver.disconnect()
        return None if len(entities) <= 0 else entities[0]

    def select_by_param(self, param: Dict) -> Entity:
        entities: List[Entity] = []
        try:
            self.db_driver.connect()
            query = self.query_factory.\
                create_select_query_by_param(self.entity_type(), param.keys())
            rows = self.db_driver.fetch_with_param(query, param)
            entities = self.entity_service.create_entity_list(rows)
        except Exception:
            self.logger.error(traceback.format_exc())
        finally:
            self.db_driver.disconnect()
        return entities

    def insert(self, entities: List[Entity]) -> int:
        try:
            self.db_driver.connect(is_transaction=True)
            query = self.query_factory.create_insert_query(
                entities[0],
                len(entities)
            )
            params = self._create_param_extra_insert_require(entities)
            rows = self.db_driver.execute(query, params)
            self.db_driver.commit()
        except Exception:
            self.db_driver.rollback()
            self.logger.error(traceback.format_exc())
        finally:
            self.db_driver.disconnect()
        return rows

    def update(self, entity: Entity) -> int:
        try:
            self.db_driver.connect(is_transaction=True)
            query = self.query_factory.create_update_query_by_id(entity)
            set_params = entity.get_is_insert_required_items()
            where_params = entity.get_primary_colum_values()
            effect_row_count = self.db_driver.execute(query, set_params + where_params)
            self.db_driver.commit()
        except Exception:
            self.db_driver.rollback()
            self.logger.error(traceback.format_exc())
        finally:
            self.db_driver.disconnect()
        return effect_row_count

    def delete(self, entity: Entity) -> int:
        try:
            self.db_driver.connect(is_transaction=True)
            query = self.query_factory.create_delete_query_by_id(entity)
            where_params = entity.get_primary_colum_values()
            effect_row_count = self.db_driver.execute(query, where_params)
            self.db_driver.commit()
        except Exception:
            self.db_driver.rollback()
            self.logger.error(traceback.format_exc())
        finally:
            self.db_driver.disconnect()
        return effect_row_count

    def _create_param_extra_insert_require(self, entities: List[Entity]) -> List[str]:
        params = []
        for entity in entities:
            for value in entity.__dict__.values():
                if value.is_insert_require:
                    params.append(value.value)

        return params
