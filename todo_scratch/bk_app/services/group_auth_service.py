from todo_scratch.bk_app.enums.group_auth_type_enum import GroupAuthTypeEnum
from todo_scratch.bk_app.enums.group_user_state_enum import GroupUserStateEnum
from todo_scratch.bk_app.repositories.group_repository import GroupRepository


class GroupAuthService:
    """グループ認証サービス
    グループの所属情報を取得するためのサービスクラスです

    """

    @staticmethod
    def exist_group(group_id: int) -> bool:
        return True

    @staticmethod
    def is_join_to_group(user_id: int, group_id: int) -> bool:
        """グループに参加しているか判定

        Args:
            user_id (int): ユーザID
            group_id (int): グループID

        Returns:
            bool: グループの参加有無
        """
        group_repository = GroupRepository()
        group_belongs_entities = group_repository.get_group_belongs_by_id(
            user_id=user_id,
            group_id=group_id
        )
        if len(group_belongs_entities) <= 0:
            return False
        return group_belongs_entities[0].user_status.value == int(GroupUserStateEnum.APPROVED)

    @staticmethod
    def is_host_user_in_group(user_id: int, group_id: int) -> bool:
        """グループのホストユーザであるか判定

        Args:
            user_id (int): ユーザID
            group_id (int): グループiD

        Returns:
            bool: ホストユーザであるかの有無
        """
        group_repository = GroupRepository()
        group_belongs_entities = group_repository.get_group_belongs_by_id(
            user_id=user_id,
            group_id=group_id
        )
        if len(group_belongs_entities) <= 0:
            return False
        return group_belongs_entities[0].user_status.value == int(GroupUserStateEnum.APPROVED) and \
            group_belongs_entities[0].auth_type.value == int(GroupAuthTypeEnum.HOST)
