from todo_scratch.bk_base.db.entities.entity import Entity
from todo_scratch.bk_base.db.entities.items import items


class TaskDetailEntity(Entity):
    """タスクの詳細情報エンティティ

    Args:
        Entity (_type_): エンティティ基底クラス
    """

    def __init__(self) -> None:
        self.task_id = items.IntItem(is_praimary=True, is_insert_require=False)
        self.group_id = items.IntItem()
        self.user_id = items.IntItem()
        self.user_name = items.CharItem(length=100)
        self.task_status_id = items.IntItem()
        self.title = items.CharItem(length=100)
        self.context = items.TextItem()
        self.deadline_at = items.DatetimeItem()
        self.created_at = items.DatetimeItem(is_insert_require=False)
        self.updated_at = items.DatetimeItem(is_insert_require=False)
        super().__init__()
