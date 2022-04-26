from typing import Dict, List

from todo_scratch.bk_base.db.entities.items.base_item import BaseItem


class Entity:

    table_name = None

    @classmethod
    def create_instance(cls):
        pass

    @classmethod
    def convert_to_entity(cls, query_result: Dict):
        """Queryの結果をentityへ変換
        """
        for key, value in query_result.items():
            item = getattr(cls, key, None)
            if not item or not isinstance(item, BaseItem):
                continue
            item.set_value(value)

        return cls

    @classmethod
    def convert_to_entity_list(self,) -> List:
        pass

    def convert_to_param(self,):
        """Entityをパラメータへ変換
        """
        pass

    def validate(self,):
        pass
