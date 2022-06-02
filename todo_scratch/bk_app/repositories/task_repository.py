
import datetime
from typing import Dict, List
from todo_scratch.bk_app.entities.comment_entity import CommentEntity
from todo_scratch.bk_app.entities.history_entity import HistoryEntity
from todo_scratch.bk_app.entities.task_entity import TaskEntity
from todo_scratch.bk_app.entities.task_history_entity import TaskHistoryEntity
from todo_scratch.bk_app.entities.task_status_entity import TaskStatusEntity
from todo_scratch.bk_app.entities.task_with_postuser_entity import TaskWithPostUserEntity
from todo_scratch.bk_base.db.db_accesors.db_accesor import DbAccesor
from todo_scratch.bk_base.db.db_accesors.select_db_accesor import SelectDbAccesor


class TaskRepository:
    """タスクテーブルの永続化処理をまとめたクラス
    """

    get_task_list_query = """
    SELECT
        ts_task.*,
        ts_user.user_name
    FROM todo_scratch.task as ts_task
    LEFT JOIN todo_scratch.`user` as ts_user
    ON ts_task.user_id = ts_user.user_id
    WHERE group_id = %(group_id)s
    {0}
    AND deadline_at >= %(deadline_at_from)s
    AND deadline_at <= %(deadline_at_to)s
    ORDER BY {1}
    """

    get_task_hisotry_query = """
    SELECT
    task_history.*
    FROM(

        SELECT
            ts_comment.user_id as post_user_id,
            ts_comment.task_id,
            ts_comment.`comment` as context,
            ts_comment.created_at,
            ts_comment.updated_at
        FROM todo_scratch.`comment` as ts_comment
        UNION ALL
        SELECT
            0 as post_user_id,
            ts_history.task_id,
            ts_history.history_text as context,
            ts_history.created_at,
            ts_history.updated_at
            FROM todo_scratch.history as ts_history
    ) as task_history
    ORDER BY task_history.created_at
    """

    def get_task_list(self,
                      group_id: int,
                      task_status_id=0,
                      title='',
                      post_user_id=0,
                      deadline_at_from=datetime.datetime(1900, 1, 1),
                      deadline_at_to=datetime.datetime(2999, 12, 31),
                      order_by_text="deadline_at desc") -> List[TaskWithPostUserEntity]:
        """タスクの取得

        Args:
            group_id (int): グループID
            task_status_id (int, optional): タスクステータスID. Defaults to 0.
            title (str, optional): タイトル. Defaults to ''.
            post_user_id (int, optional): 投稿ユーザ. Defaults to 0.
            deadline_at_from (str, optional): 期限開始日時. Defaults to "".
            deadline_at_to (str, optional): 期限終了日時. Defaults to "".

        Returns:
            List[TaskWithPostUserEntity]: タスクエンティティリスト
        """

        select_db_accesor = SelectDbAccesor(TaskWithPostUserEntity)

        query_param: Dict = {}
        query_param["group_id"] = group_id
        add_where_query = ""
        if not task_status_id == 0:
            add_where_query += " AND task_status_id = %(task_status_id)s"
            query_param["task_status_id"] = task_status_id
        if len(title) > 0:
            add_where_query += " AND title LIKE CONCAT('%', %(title)s, '%')"
            query_param["title"] = title
        if not post_user_id == 0:
            add_where_query += " AND user_id = %(post_user_id)s"
            query_param["post_user_id"] = post_user_id

        query_param["deadline_at_from"] = deadline_at_from
        query_param["deadline_at_to"] = deadline_at_to

        query = self.get_task_list_query.format(add_where_query, order_by_text)
        return select_db_accesor.select(
            query=query,
            param=query_param
        )

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

    def get_task_by_task_id(self, task_id: int, group_id: int,) -> List[TaskEntity]:
        """指定したタスクIDのタスクの取得

        Args:
            task_id (int): タスクID
            group_id (int): グループID

        Returns:
            _type_: タスクエンティティリスト
        """
        db_accesor = DbAccesor(TaskEntity)
        return db_accesor.select_by_param(
            param={
                "task_id": task_id,
                "group_id": group_id
            }
        )

    def get_task_history(self, task_id: int) -> List[TaskHistoryEntity]:
        """タスクコメント・履歴統合情報の取得

        Args:
            task_id (int): タスクID

        Returns:
            List[TaskHistoryEntity]:タスクコメント・履歴統合情報エンティティリスト
        """
        select_db_accesor = SelectDbAccesor(TaskHistoryEntity)
        return select_db_accesor.select(
            query=self.get_task_hisotry_query,
            param={
                "task_id": task_id
            }
        )

    def insert_task(self, task_entity: TaskEntity) -> int:
        """タスクの追加

        Args:
            task_entity (TaskEntity): 追加するタスクエンティティ

        Returns:
            int: 追加したタスクID
        """
        db_accesor = DbAccesor(TaskEntity)
        return db_accesor.insert(task_entity)

    def insert_task_comment(self, task_comment_entity: CommentEntity) -> int:
        """タスクコメントの追加

        Args:
            task_comment_entity (CommentEntity): タスクコメントエンティティ

        Returns:
            int: 追加したタスクコメントID
        """

        db_accesor = DbAccesor(CommentEntity)
        return db_accesor.insert(task_comment_entity)

    def insert_task_history(self, task_hisotry_entity: HistoryEntity) -> int:
        """タスク履歴の追加

        Args:
            task_hisotry_entity (HistoryEntity): タスク履歴エンティティ

        Returns:
            int: 追加したタスク履歴ID
        """

        db_accesor = DbAccesor(HistoryEntity)
        return db_accesor.insert(task_hisotry_entity)

    def update_task(self, task_entity: TaskEntity) -> int:
        """タスクの更新

        Args:
            task_entity (TaskEntity): 更新するタスクエンティティ

        Returns:
            int: 更新したタスクID
        """
        db_accesor = DbAccesor(TaskEntity)
        return db_accesor.update(task_entity)

    def delete_task(self, task_entites: List[TaskEntity]) -> int:
        """タスクの削除

        Args:
            task_entites (List[TaskEntity]): 削除するタスクエンティティ

        Returns:
            int: 削除したレコード数
        """
        db_accesor = DbAccesor(TaskEntity)
        return db_accesor.delete_bulk(task_entites)

    def get_task_status_by_group_id(self, group_id: int) -> List[TaskStatusEntity]:
        """指定したグループのタスク状態マスタの取得

        Args:
            group_id (int): グループID

        Returns:
            List[TaskStatusEntity]: タスク情報エンティティ
        """
        db_accesor = DbAccesor(TaskStatusEntity)
        return db_accesor.select_by_param(
            param={
                "group_id": group_id
            }
        )
