from todo_scratch.bk_base.db.entities.entity import Entity
from todo_scratch.bk_base.db.entities.items import items


class UserEntity(Entity):

    table_name = "user"

    user_id = items.IntItem()
    name = items.CharItem()
    age = items.IntItem()
    context = items.TextItem()
    created_at = items.DatetimeItem()
    update_at = items.DatetimeItem()
