from todo_scratch.bk_base.db.entities.entity import Entity
from todo_scratch.bk_base.db.entities.items import items


class TaskEntity(Entity):
    table_name = "todo_scratch.task"

    def __init__(self) -> None:
        self.task_id = items.IntItem(is_praimary=True, is_insert_require=False)
        self.group_id = items.IntItem()
        self.user_id = items.IntItem()
        self.task_status_id = items.IntItem()
        self.title = items.CharItem(length=50)
        self.context = items.TextItem()
        self.deadline_at = items.DatetimeItem()
        self.created_at = items.DatetimeItem(is_insert_require=False)
        self.updated_at = items.DatetimeItem(is_insert_require=False)
        super().__init__()

    def set_entity_values(self, group_id, user_id, title, task_status_id, context, deadline_at):
        self.group_id.set_value(group_id)
        self.user_id.set_value(user_id)
        self.task_status_id.set_value(task_status_id)
        self.title.set_value(title)
        self.context.set_value(context)
        self.deadline_at.set_value(deadline_at)

    @staticmethod
    def create_instance(group_id, user_id, title, task_status_id, context, deadline_at):
        entity = TaskEntity()
        entity.set_entity_values(group_id, user_id, title, task_status_id, context, deadline_at)
        return entity
