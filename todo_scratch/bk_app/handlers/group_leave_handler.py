from xmlrpc.client import Boolean
from todo_scratch.bk_app.repositories.group_repository import GroupRepository


class GroupLeaveHandler:
    """グループ離脱ハンドラー
    """

    def __init__(self) -> None:
        self.group_repository = GroupRepository()

    def leave_group(self, user_id: int, group_id: int) -> Boolean:
        """グループの離脱処理
        グループ所属情報を削除します

        Args:
            user_id (int): ユーザID
            group_id (int): グループID

        Returns:
            Boolean: 削除成功有無
        """
        group_belongs_entities = self.group_repository.get_group_belongs_by_id(
            user_id=user_id,
            group_id=group_id
        )

        if len(group_belongs_entities) <= 0:
            return False

        return self.group_repository.delete_group_belongs_bulk(group_belongs_entities) > 0
