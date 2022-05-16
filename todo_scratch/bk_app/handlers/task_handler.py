from typing import Dict
from todo_scratch.bk_app.entities.task_entity import TaskEntity
from todo_scratch.bk_app.repositories.task_repository import TaskRepository
from todo_scratch.bk_app.services.group_auth_service import GroupAuthService


class TaskHandler:

    def __init__(self) -> None:
        self.task_repository = TaskRepository()

    def exist_group(self, group_id: int) -> bool:
        """グループの存在有無の判定

        Args:
            group_id (int): グループID

        Returns:
            bool: グループの存在有無
        """
        return GroupAuthService.exist_group(group_id)

    def is_join_to_group(self, user_id: int, group_id: int) -> bool:
        """グループに参加しているか判定

        Args:
            user_id (int): ユーザID
            group_id (int): グループID

        Returns:
            bool: グループの参加有無
        """
        return GroupAuthService.is_join_to_group(user_id, group_id)

    def is_host_user_in_group(self, user_id: int, group_id: int) -> bool:
        """グループのホストユーザであるか判定

        Args:
            user_id (int): ユーザID
            group_id (int): グループiD

        Returns:
            bool: ホストユーザであるかの有無
        """
        return GroupAuthService.is_host_user_in_group(user_id, group_id)

    def create_task(self, group_id: int, user_id: int, param: Dict) -> bool:
        """タスクの新規追加

        Args:
            group_id (int): グループID
            user_id (int): ユーザID
            param (int): 新規追加タスク情報

        Returns:
            bool: 新規追加できたか判定
        """

        task_entity = TaskEntity.create_instance(
            group_id=group_id,
            user_id=user_id,
            task_status_id=param.get("task_status_id"),
            title=param.get("title"),
            context=param.get("context"),
            deadline_at=param.get("deadline_at")
        )

        return self.task_repository.save_task(task_entity=task_entity) > 0