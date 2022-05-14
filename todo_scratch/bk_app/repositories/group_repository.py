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

    def __init__(self) -> None:
        self.group_db_accesor = DbAccesor(GroupEntity)
        self.group_belong_db_accesor = DbAccesor(GroupBelongEntity)

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
        return self.group_belong_db_accesor.insert(group_belongs_entity)

    def save_group_belongs_list(self, group_belongs_entities: List[GroupBelongEntity]) -> int:
        """グループ所属情報の複数

        Args:
            group_entity (GroupEntity): 複数するグループ所属情報のエンティティ

        Returns:
            int: 複数したグループ所属情報の数
        """
        return self.group_belong_db_accesor.insert_bulk(group_belongs_entities)

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
