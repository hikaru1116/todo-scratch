from copy import deepcopy
import datetime
from typing import Any, Dict, List
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

    def _get_query_param(self, param: Dict, key: str, data_type: type, default_value: Any) -> Any:
        value_list = param.get(key, [])
        if len(value_list) <= 0:
            return default_value

        value = value_list[0]
        try:
            return data_type(value)
        except Exception:
            return default_value

    def get_task(self, group_id: int, query_param: Dict) -> List[Dict]:
        """タスクの取得

        Args:
            group_id (int): グループID
            param (Dict): 検索クエリパラメータ

        Returns:
            List[Dic]: タスクエンティティ情報
        """
        task_status_id = self._get_query_param(query_param, "task_status_id", str, 0)
        title = self._get_query_param(query_param, "title", str, "")
        post_user_id = self._get_query_param(query_param, "post_user_id", int, 0)
        deadline_at_from = self._get_query_param(query_param, "deadline_at_from", str, "1900-01-01T01:01:00")
        deadline_at_to = self._get_query_param(query_param, "deadline_at_to", str, "2999-12-31T12:00:00")

        task_entities = self.task_repository.get_task_list(
            group_id=group_id,
            task_status_id=task_status_id,
            title=title,
            post_user_id=post_user_id,
            deadline_at_from=datetime.datetime.strptime(deadline_at_from, '%Y-%m-%dT%H:%M:%S'),
            deadline_at_to=datetime.datetime.strptime(deadline_at_to, '%Y-%m-%dT%H:%M:%S'),
        )
        list = []
        for task_entity in task_entities:
            row: Dict = {}
            row["task_id"] = task_entity.task_id.value
            row["user_id"] = task_entity.user_id.value
            row["title"] = task_entity.title.value
            row["context"] = task_entity.context.value
            row["deadline_at"] = task_entity.deadline_at.to_dict_value
            row["task_status_id"] = task_entity.task_status_id.value
            row["created_at"] = task_entity.created_at.to_dict_value
            row["updated_at"] = task_entity.updated_at.to_dict_value

            list.append(row)

        return list

    def get_task_divide_by_task(self, group_id: int):
        task_entities = self.task_repository.get_task_list(
            group_id=group_id,
            order_by_text="task_status_id, updated_at DESC"
        )

        before_task_statu_id = -1
        result: List = []
        list_data: Dict = {}
        now = datetime.datetime.now()
        for entity in task_entities:
            if before_task_statu_id < 0 or before_task_statu_id != entity.task_status_id.value:
                if len(list_data) > 0:
                    list_data_copy = deepcopy(list_data)
                    result.append(list_data_copy)
                    list_data = {}

                list_data["task_status_id"] = entity.task_status_id.value
                list_data["task_list"] = []
                before_task_statu_id = entity.task_status_id.value

            task: Dict = {}
            task["task_id"] = entity.task_id.value
            task["user_id"] = entity.user_id.value
            task["user_name"] = entity.user_name.value
            task["title"] = entity.title.value
            task["context"] = entity.context.value
            task["deadline_at"] = entity.deadline_at.to_dict_value
            task["is_expired"] = now > entity.deadline_at.value
            task["task_status_id"] = entity.task_status_id.value
            task["created_at"] = entity.created_at.to_dict_value
            task["updated_at"] = entity.updated_at.to_dict_value

            list_data["task_list"].append(task)

        list_data_copy = deepcopy(list_data)
        result.append(list_data_copy)

        return result

    def get_task_detail(self, task_id: int, group_id: int) -> Dict:
        """タスク詳細情報の取得

        Args:
            task_id (int): タスクID
            group_id (int): グループID

        Returns:
            Dict: タスク詳細情報
        """

        task_entities = self.task_repository.get_task_by_task_id(task_id, group_id)
        if len(task_entities) <= 0:
            return {}

        select_task_entity = task_entities[0]

        task_history_entities = self.task_repository.get_task_history(task_id)
        result: Dict = {}
        result["task_id"] = select_task_entity.task_id.to_dict_value
        result["group_id"] = select_task_entity.group_id.to_dict_value
        result["user_id"] = select_task_entity.user_id.to_dict_value
        result["title"] = select_task_entity.title.to_dict_value
        result["context"] = select_task_entity.context.to_dict_value
        result["deadline_at"] = select_task_entity.deadline_at.to_dict_value
        result["task_status_id"] = select_task_entity.task_status_id.to_dict_value
        task_history_list: List = []
        task_hisotry_id = 0
        for task_history_entity in task_history_entities:
            task_hisotry_id += 1
            task_history_list.append(
                {
                    "task_hisotry_id": task_hisotry_id,
                    "is_system_post": (not task_history_entity.post_user_id.value == 0),  # 投稿ユーザがシステムユーザ(0)であるか判定
                    "user_id": task_history_entity.post_user_id.to_dict_value,
                    "context": task_history_entity.context.to_dict_value,
                    "created_at": task_history_entity.created_at.to_dict_value,
                    "updated_at": task_history_entity.updated_at.to_dict_value,
                }
            )
        result["history"] = task_history_list

        return result

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
