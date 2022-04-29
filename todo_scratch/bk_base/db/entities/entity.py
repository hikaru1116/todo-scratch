from typing import Dict
from todo_scratch.bk_base.db.entities.items.base_item import BaseItem


class Entity:

    table_name = None

    def set_values_by_row(cls, row: Dict):
        """Queryの結果をentityへ変換
        """
        for key, value in row.items():
            item = getattr(cls, key, None)
            if not item or not isinstance(item, BaseItem):
                continue
            item.set_value(value)

    def convert_to_param(self,):
        """Entityをパラメータへ変換
        """
        pass

    def validate(self,):
        pass

    def count_is_insert_required_item(self,):
        count = 0
        for value in self.__dict__.values():
            if not hasattr(value, "is_insert_require"):
                continue
            if value.is_insert_require:
                count += 0
        return count
