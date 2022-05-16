from todo_scratch.bk_base.db.entities.entity import Entity
from todo_scratch.bk_base.db.entities.items import items


class History(Entity):
    table_name = "todo_scratch.history"

    def __init__(self) -> None:
        self.history_text_id = items.IntItem(is_praimary=True, is_insert_require=False)
        self.task_id = items.IntItem()
        self.history_text = items.TextItem()
        self.created_at = items.DatetimeItem(is_insert_require=False)
        self.updated_at = items.DatetimeItem(is_insert_require=False)
        super().__init__()

    def set_entity_values(self, task_id, history_text):
        self.task_id.set_value(task_id)
        self.history_text.set_value(history_text)

    @staticmethod
    def create_instance(group_id, history_text,):
        entity = History()
        entity.set_entity_values(group_id, history_text,)
        return entity
