from functools import wraps
import logging
import traceback
from typing import Callable, Dict, List
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
            rows = self.db_driver.query_with_param(query, ())
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
            rows = self.db_driver.query_with_param(query, (id,))
            entities = self.entity_service.create_entity_list(rows)
        except Exception:
            self.logger.error(traceback.format_exc())
        finally:
            self.db_driver.disconnect()
        return entities

    def select_by_param(self, param: Dict) -> Entity:
        entities: List[Entity] = []
        try:
            self.db_driver.connect()
            query = self.query_factory.\
                create_select_query_by_param(self.entity_type(), param.keys())
            rows = self.db_driver.query_with_param(query, param)
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
            print(query, params)
            rows = self.db_driver.execute(query, params)
            self.db_driver.commit()
        except Exception:
            self.db_driver.rollback()
            self.logger.error(traceback.format_exc())
        finally:
            self.db_driver.disconnect()
        return rows

    def update(self,):
        pass

    def delete(self,):
        pass

    def exception_callback(self,):
        self.logger.error(traceback.format_exc())

    def final_callback(self,):
        self.db_driver.disconnect()

    def _create_param_extra_insert_require(self, entities: List[Entity]) -> List[str]:
        params = []
        for entity in entities:
            for value in entity.__dict__.values():
                if value.is_insert_require:
                    params.append(value.value)

        return params


def exception_handling(exception_callback: Callable,
                       final_callback: Callable):
    def exception_handling_wrapper(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
            except Exception:
                exception_callback()
            finally:
                final_callback()
            return result
        return wrapper
    return exception_handling_wrapper
