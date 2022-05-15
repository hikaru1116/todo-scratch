from todo_scratch.bk_base.db.entities.entity import Entity
from todo_scratch.bk_base.db.entities.items import items


class TaskStatusEntity(Entity):
    table_name = "task_status"

    def __init__(self) -> None:
        self.task_status_id = items.IntItem(is_praimary=True, is_insert_require=False)
        self.group_id = items.VcharItem()
        self.task_status_name = items.VcharItem()
        self.status_color = items.VcharItem()
        self.created_at = items.DatetimeItem(is_insert_require=False)
        self.updated_at = items.DatetimeItem(is_insert_require=False)
        super().__init__()

    def set_entity_values(self, group_id, task_status_name, staus_color):
        self.group_id.set_value(group_id)
        self.task_status_name.set_value(task_status_name)
        self.status_color.set_value(staus_color)

    @staticmethod
    def create_instance(group_id, task_status_name, staus_color):
        entity = TaskStatusEntity()
        entity.set_entity_values(group_id, task_status_name, staus_color)
        return entity
