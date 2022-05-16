
from typing import List
from todo_scratch.bk_app.entities.task_entity import TaskEntity
from todo_scratch.bk_base.db.db_accesors.db_accesor import DbAccesor


class TaskRepository:
    """タスクテーブルの永続化処理をまとめたクラス
    """

    def get_task_by_id(self, task_id: int, group_id: int, user_id: int) -> List[TaskEntity]:
        """指定したIDのタスクの取得

        Args:
            task_id (int): タスクID
            group_id (int): グループID
            user_id (int): ユーザID

        Returns:
            _type_: タスクエンティティリスト
        """
        db_accesor = DbAccesor(TaskEntity)
        return db_accesor.select_by_param(
            param={
                "task_id": task_id,
                "group_id": group_id,
                "user_id": user_id
            }
        )

    def save_task(self, task_entity: TaskEntity) -> int:
        """タスクの追加

        Args:
            task_entity (TaskEntity): 追加するタスクエンティティ

        Returns:
            int: 追加したタスクID
        """
        db_accesor = DbAccesor(TaskEntity)
        return db_accesor.insert(task_entity)

    def update_task(self, task_entity: TaskEntity) -> int:
        """タスクの更新

        Args:
            task_entity (TaskEntity): 更新するタスクエンティティ

        Returns:
            int: 更新したタスクID
        """
        db_accesor = DbAccesor(TaskEntity)
        return db_accesor.update(task_entity)
