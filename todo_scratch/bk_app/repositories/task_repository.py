
from typing import List
from todo_scratch.bk_app.entities.comment_entity import CommentEntity
from todo_scratch.bk_app.entities.history_entity import HistoryEntity
from todo_scratch.bk_app.entities.task_entity import TaskEntity
from todo_scratch.bk_app.entities.task_status_entity import TaskStatusEntity
from todo_scratch.bk_base.db.db_accesors.db_accesor import DbAccesor
from todo_scratch.bk_base.db.db_accesors.select_db_accesor import SelectDbAccesor


class TaskRepository:
    """タスクテーブルの永続化処理をまとめたクラス
    """

    # get_task_list_query = """
    # SELECT
    #     *
    # FROM todo_scratch.task
    # WHERE group_id = 44
    # AND task_status_id = 19
    # AND title LIKE '%ta%'
    # AND user_id = 1
    # AND deadline_at >= '2022-05-16 23:56:26'
    # AND deadline_at <= '2022-05-30 23:56:26'
    # """

    get_task_list_query = """
    SELECT
        *
    FROM todo_scratch.task
    WHERE group_id = %(group_id)s
    """

    def get_task_list(self,
                      group_id: int,
                      task_status_id=0,
                      title='',
                      post_user_id=0,
                      deadline_at_from="",
                      deadline_at_to="") -> List[TaskEntity]:
        """タスクの取得

        Args:
            group_id (int): グループID
            task_status_id (int, optional): タスクステータスID. Defaults to 0.
            title (str, optional): タイトル. Defaults to ''.
            post_user_id (int, optional): 投稿ユーザ. Defaults to 0.
            deadline_at_from (str, optional): 期限開始日時. Defaults to "".
            deadline_at_to (str, optional): 期限終了日時. Defaults to "".

        Returns:
            List[TaskEntity]: タスクエンティティリスト
        """

        select_db_accesor = SelectDbAccesor(TaskEntity)

        return select_db_accesor.select(
            query=self.get_task_list_query,
            param={
                "group_id": group_id
            }
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
