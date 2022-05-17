from todo_scratch.bk_base.db.entities.entity import Entity
from todo_scratch.bk_base.db.entities.items import items


class TaskHistoryEntity(Entity):
    """タスクコメント・履歴統合エンティティ

    Args:
        Entity (_type_): エンティティ基底クラス
    """

    def __init__(self) -> None:
        self.post_user_id = items.IntItem()
        self.task_id = items.IntItem()
        self.context = items.TextItem()
        self.created_at = items.DatetimeItem()
        self.updated_at = items.DatetimeItem()
        super().__init__()
