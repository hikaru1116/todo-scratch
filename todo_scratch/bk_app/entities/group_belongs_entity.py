from todo_scratch.bk_base.db.entities.entity import Entity
from todo_scratch.bk_base.db.entities.items import items


class GroupBelongEntity(Entity):
    table_name = "group_belongs"

    def __init__(self) -> None:
        self.group_belongs_id = items.IntItem(is_praimary=True, is_insert_require=False)
        self.group_id = items.IntItem()
        self.user_id = items.IntItem()
        self.auth_type = items.IntItem()
        self.user_status = items.IntItem()
        self.is_selected = items.BoolItem()
        self.created_at = items.DatetimeItem(is_insert_require=False)
        self.updated_at = items.DatetimeItem(is_insert_require=False)
        super().__init__()

    def set_entity_values(self, group_id, user_id, auth_type, user_status, is_selected):
        self.group_id.set_value(group_id)
        self.user_id.set_value(user_id)
        self.auth_type.set_value(auth_type)
        self.user_status.set_value(user_status)
        self.is_selected.set_value(is_selected)

    @staticmethod
    def create_instance(group_id, user_id, auth_type, user_status, is_selected):
        entity = GroupBelongEntity()
        entity.set_entity_values(group_id, user_id, auth_type, user_status, is_selected)
        return entity
