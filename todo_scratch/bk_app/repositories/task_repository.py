
from todo_scratch.bk_app.entities.task_entity import TaskEntity
from todo_scratch.bk_base.db.db_accesors.db_accesor import DbAccesor


class TaskRepository:
    """タスクテーブルの永続化処理をまとめたクラス
    """

    def save_task(self, task_entity: TaskEntity) -> int:
        """タスクの追加

        Args:
            task_entity (TaskEntity): 追加するタスクエンティティ

        Returns:
            int: 追加したタスクID
        """
        db_accesor = DbAccesor(TaskEntity)
        return db_accesor.insert(task_entity)
