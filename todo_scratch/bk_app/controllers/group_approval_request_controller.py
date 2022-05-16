from typing import List
from todo_scratch.bk_app.entities.group_detail_entity import GroupDetailEntity
from todo_scratch.bk_app.entities.user_entity import UserEntity
from todo_scratch.bk_app.handlers.group_approcal_request_handler import GroupApprovalRequestHandler
from todo_scratch.bk_base.controller.controller import Controller
from todo_scratch.bk_base.http.request import Request
from todo_scratch.bk_base.http.response.json_response import JSONResponse
from todo_scratch.bk_base.http.response.response import Response


class GroupApprovalRequestController(Controller):
    """グループ承認リクエストコントローラ
    ApiUrl[/group/approval-request]のメソッドをまとめたクラスです

    Args:
        Controller (_type_): コントローラ基底クラス
    """

    def get(self, request: Request, user: UserEntity, **kwargs) -> Response:

        group_detail_entities: List[GroupDetailEntity] = \
            self._get_handler().get_un_approved_group_list(user.user_id.value)

        if len(group_detail_entities) <= 0:
            return Response()

        result = []
        for group_detail_entity in group_detail_entities:
            result.append(group_detail_entity.to_dict())

        return JSONResponse(
            dic=result
        )

    def post(self, request: Request, user: UserEntity) -> Response:
        return JSONResponse()

    def _get_handler(self):
        return GroupApprovalRequestHandler()
