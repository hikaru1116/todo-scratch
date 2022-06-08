from typing import Dict, List
from todo_scratch.bk_app.entities.group_detail_entity import GroupDetailEntity
from todo_scratch.bk_app.entities.user_entity import UserEntity
from todo_scratch.bk_app.enums.group_user_state_enum import GroupUserStateEnum
from todo_scratch.bk_app.handlers.group_approcal_request_handler import GroupApprovalRequestHandler
from todo_scratch.bk_app.handlers.group_handler import GroupHandler
from atom_bk_frame.controller.controller import Controller
from atom_bk_frame.http.request import Request
from atom_bk_frame.http.response.http_error_response import Response404
from atom_bk_frame.http.response.json_response import JSONResponse
from atom_bk_frame.http.response.response import Response


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
            return JSONResponse(dic={})

        result = []
        for group_detail_entity in group_detail_entities:
            result.append(group_detail_entity.to_dict())

        return JSONResponse(
            dic=result
        )

    def post(self, request: Request, user: UserEntity, **kwargs) -> Response:
        print("found GroupApprovalRequestController")
        body: Dict = request.json
        group_id = body.get('group_id', None)

        if group_id is None:
            return Response404()

        group_handler = self._get_group_handler()

        if group_handler.is_join_to_group(user.user_id.value, group_id):
            print("is_join_to_group")
            return Response404()

        if not group_handler.update_group_belongs_by_user_status(user.user_id.value, group_id, GroupUserStateEnum.APPROVED):
            return Response404()

        return JSONResponse(
            dic=group_handler.get_detail_group_info(user.user_id.value, group_id)
        )

    def _get_handler(self):
        return GroupApprovalRequestHandler()

    def _get_group_handler(self,):
        return GroupHandler()
