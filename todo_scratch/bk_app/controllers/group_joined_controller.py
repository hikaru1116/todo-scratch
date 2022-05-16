from typing import List
from todo_scratch.bk_app.entities.group_detail_entity import GroupDetailEntity
from todo_scratch.bk_app.entities.user_entity import UserEntity
from todo_scratch.bk_app.enums.group_user_state_enum import GroupUserStateEnum
from todo_scratch.bk_app.repositories.group_repository import GroupRepository
from todo_scratch.bk_base.controller.controller import Controller
from todo_scratch.bk_base.http.request import Request
from todo_scratch.bk_base.http.response.json_response import JSONResponse
from todo_scratch.bk_base.http.response.response import Response


class GroupJoinedController(Controller):
    """ユーザのグループ参加情報コントローラ
    ApiUrl[/group/joined]のメソッドをまとめたクラスです

    Args:
        Controller (_type_): コントローラ基底クラス
    """

    def get(self, request: Request, user: UserEntity, **kwargs) -> Response:

        group_detail_entities: List[GroupDetailEntity] = self._get_handler().get_joined_group_list(user.user_id.value)
        if len(group_detail_entities) <= 0:
            return JSONResponse(dic={})

        result = []
        for group_detail_entity in group_detail_entities:
            result.append(group_detail_entity.to_dict())

        return JSONResponse(
            dic=result
        )

    def _get_handler(self,):
        return GroupJoinedHandler()


class GroupJoinedHandler:
    """グループ参加情報コントローラハンドラー
    """

    def __init__(self) -> None:
        self.group_repository = GroupRepository()

    def get_joined_group_list(self, user_id: int) -> List[GroupDetailEntity]:
        """参加済みのグループ一覧をの取得

        Args:
            user_id (int): ユーザID

        Returns:
            List[GroupDetailEntity]: 詳細なグループ情報エンティティ
        """
        return self.group_repository.get_detail_group_by_user_status(
            user_id=user_id,
            user_status=GroupUserStateEnum.APPROVED
        )
