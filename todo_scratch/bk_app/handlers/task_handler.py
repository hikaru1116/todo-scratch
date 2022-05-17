from typing import Dict, List
from todo_scratch.bk_app.entities.comment_entity import CommentEntity
from todo_scratch.bk_app.entities.history_entity import HistoryEntity
from todo_scratch.bk_app.entities.task_entity import TaskEntity
from todo_scratch.bk_app.entities.task_status_entity import TaskStatusEntity
from todo_scratch.bk_app.entities.user_entity import UserEntity
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

    def get_task_status_list(self, group_id) -> List[Dict]:
        """タスクステータス情報の取得

        Args:
            group_id (_type_): グループID

        Returns:
            List[Dict]: タスクステータス情報エンティティリスト
        """
        entities: List[TaskStatusEntity] = self.task_repository.get_task_status_by_group_id(
            group_id=group_id
        )

        list = []
        for entity in entities:
            list.append(
                {
                    "task_status_id": entity.task_status_id.value,
                    "group_id": entity.group_id.value,
                    "task_status_name": entity.task_status_name.value,
                    "status_color": entity.status_color.value
                }
            )
        return list

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

        return self.task_repository.insert_task(task_entity=task_entity) > 0

    def post_task_comment(self, task_id: int, user_id: int, comment: str) -> int:
        """タスクコメントの追加

        Args:
            task_id (int): タスクID
            user_id (int): ユーザID
            comment (str): コメントテキスト

        Returns:
            int: 追加したタスクコメントのID
        """
        comment_entity = CommentEntity.create_instance(
            task_id=task_id,
            user_id=user_id,
            comment=comment
        )

        return self.task_repository.insert_task_comment(comment_entity)

    def _insert_task_history(self, task_id: int, hitory_text: str, inner_texts=()) -> int:
        """タスク履歴の追加

        Args:
            task_id (int): 追加するタスクID
            hitory_text (str): 履歴テキスト
            post_user_name (str, optional): 履歴テキストに含める文字列. Defaults to "".

        Returns:
            int: _description_
        """

        task_history_entity = HistoryEntity.create_instance(
            task_id=task_id,
            history_text=hitory_text.format(*inner_texts)
        )

        return self.task_repository.insert_task_history(task_history_entity)

    def update_task(self, task_id: int, group_id: int, user: UserEntity, param: Dict) -> bool:
        """タスクの更新

        Args:
            task_id (int): タスクID
            group_id (int): グループID
            user (UserEntity): ユーザエンティティ
            param (dict): 更新タスク情報

        Returns:
            bool: 新規追加の可否
        """

        task_entities = self.task_repository.get_task_by_id(
            task_id=task_id,
            group_id=group_id,
            user_id=user.user_id.value
        )

        if len(task_entities) <= 0:
            return False

        update_task_entity = task_entities[0]

        update_task_entity.title.set_value(param.get("title"))
        update_task_entity.context.set_value(param.get("context"))
        update_task_entity.deadline_at.set_value(param.get("deadline_at"))

        task_status_entities = self.task_repository.get_task_status_by_group_id(
            group_id=group_id
        )
        update_task_status_id = param.get("task_status_id")
        change_task_status_name = ""
        for task_status_entity in task_status_entities:
            if update_task_entity.task_status_id.value == update_task_status_id or\
                    not task_status_entity.task_status_id.value == update_task_status_id:
                continue
            change_task_status_name = task_status_entity.task_status_name.value
            update_task_entity.task_status_id.set_value(update_task_status_id)
            break

        if len(change_task_status_name) > 0:
            self._insert_task_history(
                task_id=task_id,
                hitory_text="{}が{}へ変更しました",
                inner_texts=(user.user_name.value, change_task_status_name)
            )

        self.task_repository.update_task(update_task_entity)

        return True

    def delete_task(self, task_id, group_id: int, user_id: int) -> bool:
        """タスクの削除

        Args:
            task_id (_type_): タスクID
            group_id (int): グループID
            user_id (int): ユーザID

        Returns:
            bool: 削除の可否
        """
        task_entities = self.task_repository.get_task_by_id(
            task_id=task_id,
            group_id=group_id,
            user_id=user_id
        )

        if len(task_entities) <= 0:
            return False

        return self.task_repository.delete_task(task_entities) > 0

    def change_task_status(self, task_id: int, group_id: int, user: UserEntity, task_status_id: int) -> bool:
        """タスクのステータスの変更

        Args:
            task_id (int): タスクID
            group_id (int): グループID
            user_id (int): ユーザID
            task_status_id (int): 変更するタスクステータスID

        Returns:
            bool: 変更の可否
        """
        task_entities = self.task_repository.get_task_by_id(
            task_id=task_id,
            group_id=group_id,
            user_id=user.user_id.value
        )

        if len(task_entities) <= 0:
            return False

        task_status_entities = self.task_repository.get_task_status_by_group_id(
            group_id=group_id
        )

        update_task_entity = task_entities[0]

        change_task_status_name = ""
        is_update = False
        for task_status_entity in task_status_entities:
            if not update_task_entity.task_status_id.value == task_status_id and\
                    task_status_entity.task_status_id.value == task_status_id:

                update_task_entity.task_status_id.set_value(
                    task_status_entity.task_status_id.value
                )
                change_task_status_name = task_status_entity.task_status_name.value
                is_update = True

        if not is_update:
            return False

        self.task_repository.update_task(update_task_entity)

        self._insert_task_history(
            task_id=task_id,
            hitory_text="{}が{}へ変更しました",
            inner_texts=(user.user_name.value, change_task_status_name)
        )

        return True
