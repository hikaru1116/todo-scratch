from typing import Dict
from todo_scratch.bk_app.entities.user_entity import UserEntity
from todo_scratch.bk_app.handlers.group_leave_handler import GroupLeaveHandler
from todo_scratch.bk_base.controller.controller import Controller
from todo_scratch.bk_base.http.request import Request
from todo_scratch.bk_base.http.response.http_error_response import Response404
from todo_scratch.bk_base.http.response.response import Response


class GroupLeaveController(Controller):
    """グループ離脱コントローラ
    ApiUrl[/group/leave]のメソッドをまとめたクラスです

    Args:
        Controller (_type_): コントローラ基底クラス
    """

    def post(self, request: Request, user: UserEntity, **kwargs) -> Response:
        body: Dict = request.json
        group_id = body.get('group_id', None)

        if group_id is None:
            return Response404()

        group_handler = self._get_group_leave_handler()

        if not group_handler.leave_group(user.user_id.value, group_id):
            return Response404()

        return Response()

    def _get_group_leave_handler(self,):
        return GroupLeaveHandler()
