from typing import List
from todo_scratch.bk_app.entities.group_belongs_entity import GroupBelongEntity
from todo_scratch.bk_app.entities.group_belongs_user_entity import GroupBelongsUserEntity
from todo_scratch.bk_app.entities.group_detail_entity import GroupDetailEntity
from todo_scratch.bk_app.entities.group_entity import GroupEntity
from todo_scratch.bk_app.entities.task_status_entity import TaskStatusEntity
from todo_scratch.bk_app.entities.user_entity import UserEntity
from todo_scratch.bk_app.enums.group_user_state_enum import GroupUserStateEnum
from todo_scratch.bk_base.db.db_accesors.db_accesor import DbAccesor
from todo_scratch.bk_base.db.db_accesors.select_db_accesor import SelectDbAccesor


class GroupRepository:
    """グループテーブルの永続化処理をまとめたクラス
    """

    user_entity_by_identifier = """
        SELECT
            user_id,
            user_name,
            email,
            `password`,
            created_at,
            updated_at
        FROM todo_scratch.`user`
        WHERE(user_name = %(user_name)s OR email = %(email)s)
    """

    get_group_belongs_with_user_entities_query = """
    SELECT
        ts_user.user_id,
        ts_user.user_name,
        ts_group_belongs.auth_type,
        ts_group_belongs.user_status
    FROM todo_scratch.group_belongs as ts_group_belongs
    INNER JOIN todo_scratch.`user` as ts_user
    ON ts_group_belongs.user_id = ts_user.user_id
    WHERE ts_group_belongs.group_id = %(group_id)s
    """

    group_belongs_by_group_id_query = """
    SELECT
        ts_group_belongs.*
    FROM todo_scratch.group_belongs as ts_group_belongs
    INNER JOIN todo_scratch.`user` as ts_user
    ON ts_group_belongs.user_id = ts_user.user_id
    WHERE ts_group_belongs.group_id = %(group_id)s
    """

    group_by_id_query = """
    SELECT
        ts_group.*
    FROM todo_scratch.`group` as ts_group
    LEFT JOIN todo_scratch.group_belongs as ts_group_belongs
    ON ts_group.group_id = ts_group_belongs.group_id
    WHERE ts_group_belongs.user_id = %(user_id)s
    AND ts_group_belongs.group_id = %(group_id)s
    """

    get_joined_group_by_user_id_query = """
    SELECT
        ts_group.group_id,
        ts_group.group_name,
        ts_group.description,
        ts_group_belongs.auth_type,
    ts_group_belongs.user_status
    FROM todo_scratch.group_belongs as ts_group_belongs
    LEFT JOIN todo_scratch.`group` as ts_group
    ON ts_group_belongs.group_id = ts_group.group_id
    WHERE ts_group_belongs.user_id = %(user_id)s
    AND ts_group_belongs.user_status = %(user_status)s
    """

    def __init__(self) -> None:
        self.group_db_accesor = DbAccesor(GroupEntity)

    def get_group_entity(self, group_id: int) -> GroupEntity:
        """グループエンティティの取得

        Args:
            group_id (int): 取得するグループのID

        Returns:
            GroupEntity: グループエンティティ
        """
        return self.group_db_accesor.select_by_id(group_id)

    def get_group_by_user_id(self, user_id, group_id: int) -> List[GroupEntity]:
        """指定したIDのグループ情報の取得

        Args:
            user_id (_type_): ユーザID

        Returns:
            List[GroupEntity]: グループエンティティ
        """
        select_db_accesor = SelectDbAccesor(GroupEntity)
        group_entities = select_db_accesor.select(
            query=self.group_by_id_query,
            param={
                "user_id": user_id,
                "group_id": group_id
            }
        )
        return group_entities

    def get_group_belongs_by_group_id(self, group_id) -> List[GroupBelongEntity]:
        """グループ所属情報の取得

        Args:
            group_id (_type_): 取得するグループのID

        Returns:
            _type_: グループ所属情報エンティティ
        """
        select_db_accesor = SelectDbAccesor(GroupBelongEntity)
        return select_db_accesor.select(
            query=self.group_belongs_by_group_id_query,
            param={
                "group_id": group_id
            }
        )

    def get_group_belongs_by_id(self, user_id: int, group_id: int) -> List[GroupBelongEntity]:
        """指定したIDからグループ所属情報を取得

        Args:
            user_id (int): ユーザID
            group_id (int): グループID

        Returns:
            List[GroupBelongEntity]: グループ所属情報エンティティリスト
        """
        db_accesor = DbAccesor(GroupBelongEntity)
        return db_accesor.select_by_param(
            param={
                "user_id": user_id,
                "group_id": group_id
            }
        )

    def get_task_status_by_group_id(self, group_id) -> List[TaskStatusEntity]:
        """指定したグループIDからタスクステータス情報を取得

        Args:
            group_id (_type_): グループID

        Returns:
            List[TaskStatusEntity]: タスクステータス情報リスト
        """
        db_accesor = DbAccesor(TaskStatusEntity)
        return db_accesor.select_by_param(
            param={
                "group_id": group_id
            }
        )

    def get_user_entity_by_identifier(self, identifier: str) -> List[UserEntity]:
        """ユーザの識別情報からユーザエンティティを取得します

        Args:
            identifier (str): ユーザ識別情報（ユーザ名またはメールアドレス）

        Returns:
            _type_: ユーザエンティティリスト
        """
        select_db_asscesor = SelectDbAccesor(UserEntity)
        return select_db_asscesor.select(
            query=self.user_entity_by_identifier,
            param={
                "user_name": identifier,
                "email": identifier
            }
        )

    def get_group_belongs_with_user_entities(self, group_id) -> List[GroupBelongsUserEntity]:
        """ユーザの権限情報とグループ所属情報の取得

        Args:
            group_id (_type_): 取得するグループのID

        Returns:
            _type_: ユーザの権限情報とグループ所属情報エンティティ
        """
        select_db_accesor = SelectDbAccesor(GroupBelongsUserEntity)
        return select_db_accesor.select(
            query=self.get_group_belongs_with_user_entities_query,
            param={
                "group_id": group_id
            }
        )

    def get_joined_group_by_user_id(self, user_id: int) -> List[GroupDetailEntity]:
        """参加済みのグループの詳細情報の取得

        Args:
            user_id (int): ユーザID

        Returns:
            List[GroupDetailEntity]: グループ詳細情報エンティティリスト
        """
        select_db_accesor = SelectDbAccesor(GroupDetailEntity)
        return select_db_accesor.select(
            query=self.get_joined_group_by_user_id_query,
            param={
                "user_id": user_id,
                "user_status": int(GroupUserStateEnum.APPROVED)
            }
        )

    def save_group(self, group_entity: GroupEntity) -> int:
        """グループの追加

        Args:
            group_entity (GroupEntity): 追加するグループのエンティティ

        Returns:
            int: 追加したグループのID
        """
        return self.group_db_accesor.insert(group_entity)

    def save_group_belongs(self, group_belongs_entity: GroupBelongEntity) -> int:
        """グループ所属情報の追加

        Args:
            group_entity (GroupEntity): 追加するグループ所属情報のエンティティ

        Returns:
            int: 追加したグループ所属情報のID
        """
        group_belong_db_accesor = DbAccesor(GroupBelongEntity)
        return group_belong_db_accesor.insert(group_belongs_entity)

    def save_group_belongs_list(self, group_belongs_entities: List[GroupBelongEntity]) -> int:
        """グループ所属情報の複数追加

        Args:
            group_entity (GroupEntity): グループ所属情報のエンティティリスト

        Returns:
            int: 追加したレコード数
        """
        group_belong_db_accesor = DbAccesor(GroupBelongEntity)
        return group_belong_db_accesor.insert_bulk(group_belongs_entities)

    def save_task_status(self, task_status_entities: List[TaskStatusEntity]) -> int:
        """タスクステータス情報の保存

        Args:
            task_status_entities (List[TaskStatusEntity]): 追加するタスクステータス情報エンティティ

        Returns:
            int: 追加したレコード数
        """
        task_status_db_accesor = DbAccesor(TaskStatusEntity)
        return task_status_db_accesor.insert_bulk(task_status_entities)

    def update_group(self, group_entity: GroupEntity) -> int:
        """グループの更新

        Args:
            group_entity (GroupEntity): 更新するグループのエンティティ

        Returns:
            int: 変更したグループのID
        """
        return self.group_db_accesor.update(group_entity)
