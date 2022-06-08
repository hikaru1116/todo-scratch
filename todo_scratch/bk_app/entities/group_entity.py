from atom_bk_frame.db.entities.entity import Entity
from atom_bk_frame.db.entities.items import items


class GroupEntity(Entity):
    """グループエンティティ

    Args:
        Entity (_type_): エンティティ基底クラス

    """
    table_name = "todo_scratch.group"

    def __init__(self) -> None:
        self.group_id = items.IntItem(is_praimary=True, is_insert_require=False)
        self.group_name = items.CharItem(length=30)
        self.description = items.TextItem()
        self.created_at = items.DatetimeItem(is_insert_require=False)
        self.updated_at = items.DatetimeItem(is_insert_require=False)
        super().__init__()

    def set_entity_values(self, group_name, description):
        self.group_name.set_value(group_name)
        self.description.set_value(description)

    @staticmethod
    def create_instance(group_name, description):
        entity = GroupEntity()
        entity.set_entity_values(group_name, description)
        return entity
