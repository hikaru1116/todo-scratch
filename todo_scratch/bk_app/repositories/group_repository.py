from typing import List
from todo_scratch.bk_app.entities.group_belongs_entity import GroupBelongEntity
from todo_scratch.bk_app.entities.group_belongs_user_entity import GroupBelongsUserEntity
from todo_scratch.bk_app.entities.group_entity import GroupEntity
from todo_scratch.bk_app.entities.user_entity import UserEntity
from todo_scratch.bk_base.db.db_accesors.db_accesor import DbAccesor
from todo_scratch.bk_base.db.db_accesors.select_db_accesor import SelectDbAccesor


class GroupRepository:
    """グループコントローラの永続化処理をまとめたクラス
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

    group_belongs_with_user_entity_query = """
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

    selected_group_by_user_id_query = """
    SELECT
        ts_group.*
    FROM todo_scratch.`group` as ts_group
    LEFT JOIN todo_scratch.group_belongs as ts_group_belongs
    ON ts_group.group_id = ts_group_belongs.group_id
    WHERE ts_group_belongs.user_id = %(user_id)s
    AND ts_group_belongs.is_selected = TRUE
    """

    selected_group_belongs_by_user_id_query = """
    SELECT
        ts_group_belongs.*
    FROM todo_scratch.`group` as ts_group
    LEFT JOIN todo_scratch.group_belongs as ts_group_belongs
    ON ts_group.group_id = ts_group_belongs.group_id
    WHERE ts_group_belongs.user_id = %(user_id)s
    AND ts_group_belongs.is_selected = TRUE
    """

    def __init__(self) -> None:
        self.group_db_accesor = DbAccesor(GroupEntity)

    def get_selected_group_by_user_id(self, user_id) -> List[GroupEntity]:
        """選択済みのグループエンティティを取得します

        Args:
            user_id (_type_): ユーザID

        Returns:
            List[GroupEntity]: グループエンティティ
        """
        select_db_accesor = SelectDbAccesor(GroupEntity)
        group_entities = select_db_accesor.select(
            query=self.selected_group_by_user_id_query,
            param={"user_id": user_id}
        )
        return group_entities

    def get_selected_group_belongs_by_user_id(self, user_id) -> List[GroupBelongEntity]:
        """選択済みのグループ所属情報エンティティを取得します

        Args:
            user_id (_type_): ユーザID

        Returns:
            List[GroupBelongEntity]: グループ所属情報エンティティ
        """
        select_db_accesor = SelectDbAccesor(GroupBelongEntity)
        group_belongs_entities = select_db_accesor.select(
            query=self.selected_group_belongs_by_user_id_query,
            param={"user_id": user_id}
        )
        return group_belongs_entities

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
        """グループ所属情報の複数

        Args:
            group_entity (GroupEntity): 複数するグループ所属情報のエンティティ

        Returns:
            int: 複数したグループ所属情報の数
        """
        group_belong_db_accesor = DbAccesor(GroupBelongEntity)
        return group_belong_db_accesor.insert_bulk(group_belongs_entities)

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

    def get_group_entity(self, group_id: int) -> GroupEntity:
        """グループエンティティの取得

        Args:
            group_id (int): 取得するグループのID

        Returns:
            GroupEntity: グループエンティティ
        """
        return self.group_db_accesor.select_by_id(group_id)

    def get_group_belongs_with_user_entities(self, group_id) -> List[GroupBelongsUserEntity]:
        """ユーザの権限情報とグループ所属情報の取得

        Args:
            group_id (_type_): 取得するグループのID

        Returns:
            _type_: ユーザの権限情報とグループ所属情報エンティティ
        """
        select_db_accesor = SelectDbAccesor(GroupBelongsUserEntity)
        return select_db_accesor.select(
            query=self.group_belongs_with_user_entity_query,
            param={
                "group_id": group_id
            }
        )

    def update_group_selected(self, user_id, select_group_id=0, is_selected_off_only=False) -> None:
        """選択中のグループを変更します

        Args:
            user_id (_type_): 変更するユーザのID
            select_group_id (int, optional): 変更先のグループのID. Defaults to 0.
            is_selected_off_only (bool, optional): 選択中であるグループをOFFにするのみにするかのフラグ. Defaults to False.
        """
        selected_group_belongs_entities = self.get_selected_group_belongs_by_user_id(user_id)
        if len(selected_group_belongs_entities) <= 0:
            return

        selected_group_belongs_entity = selected_group_belongs_entities[0]
        group_belongs_db_accesor = DbAccesor(GroupBelongEntity)
        selected_group_belongs_entity.is_selected.set_value(False)
        # すでに選択中のグループを未選択へ更新
        group_belongs_db_accesor.update(selected_group_belongs_entity)

        if not is_selected_off_only:
            # オフにするのみである場合、
            return

        group_belongs_entities = group_belongs_db_accesor.select_by_param(
            param={
                "user_id": user_id,
                "group_id": select_group_id
            }
        )
        if len(group_belongs_entities) <= 0:
            return

        group_belings_entity: GroupBelongEntity = group_belongs_entities[0]
        group_belings_entity.is_selected.set_value(True)
        # 変更先のグループを選択済みへ更新
        group_belongs_db_accesor.update(group_belings_entity)
