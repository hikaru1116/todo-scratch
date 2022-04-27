from todo_scratch.bk_base.db.entities.entity import Entity
from todo_scratch.bk_base.db.entities.items import items


class UserEntity(Entity):

    table_name = "user"

    def __init__(self) -> None:
        self.user_id = items.IntItem()
        self.name = items.CharItem()
        self.age = items.IntItem()
        self.context = items.TextItem()
        self.created_at = items.DatetimeItem()
        self.update_at = items.DatetimeItem()
        super().__init__()
