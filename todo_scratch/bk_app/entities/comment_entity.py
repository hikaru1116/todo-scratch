from todo_scratch.bk_base.db.entities.entity import Entity
from todo_scratch.bk_base.db.entities.items import items


class CommentEntity(Entity):
    table_name = "todo_scratch.comment"

    def __init__(self) -> None:
        self.comment_id = items.IntItem(is_praimary=True, is_insert_require=False)
        self.task_id = items.IntItem()
        self.user_id = items.IntItem()
        self.comment = items.TextItem()
        self.created_at = items.DatetimeItem(is_insert_require=False)
        self.updated_at = items.DatetimeItem(is_insert_require=False)
        super().__init__()

    def set_entity_values(self, task_id, user_id, comment):
        self.task_id.set_value(task_id)
        self.user_id.set_value(user_id)
        self.comment.set_value(comment)

    @staticmethod
    def create_instance(task_id, user_id, comment,):
        entity = CommentEntity()
        entity.set_entity_values(task_id, user_id, comment,)
        return entity
