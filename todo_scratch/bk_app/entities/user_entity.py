from todo_scratch.bk_base.db.entities.entity import Entity
from todo_scratch.bk_base.db.entities.items import items


class UserEntity(Entity):

    table_name = "user"

    def __init__(self) -> None:
        self.user_id = items.IntItem(is_praimary=True, is_insert_require=False)
        self.name = items.CharItem(length=10)
        self.age = items.IntItem()
        self.created_at = items.DatetimeItem(is_insert_require=False)
        self.updated_at = items.DatetimeItem(is_insert_require=False)
        super().__init__()

    def set_entity_values(self, name, age):
        self.name.set_value(name)
        self.age.set_value(age)

    @staticmethod
    def create_instance(name, age):
        user_entity = UserEntity()
        user_entity.set_entity_values(name, age)
        return user_entity
