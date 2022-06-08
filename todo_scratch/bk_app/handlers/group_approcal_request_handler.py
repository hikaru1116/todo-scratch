from typing import List
from todo_scratch.bk_app.entities.group_detail_entity import GroupDetailEntity
from todo_scratch.bk_app.enums.group_user_state_enum import GroupUserStateEnum
from todo_scratch.bk_app.repositories.group_repository import GroupRepository


class GroupApprovalRequestHandler:
    """グループ承認リクエストハンドラー
    """

    def __init__(self) -> None:
        self.group_repository = GroupRepository()

    def get_un_approved_group_list(self, user_id: int) -> List[GroupDetailEntity]:
        """未承認のグループ一覧をの取得

        Args:
            user_id (int): ユーザID

        Returns:
            List[GroupDetailEntity]: 詳細なグループ情報エンティティ
        """
        return self.group_repository.get_detail_group_by_user_status(
            user_id=user_id,
            user_status=GroupUserStateEnum.UNAPPROVED
        )
