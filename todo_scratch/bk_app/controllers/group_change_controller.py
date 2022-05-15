

from todo_scratch.bk_app.entities.user_entity import UserEntity
from todo_scratch.bk_app.handlers.group_handler import GroupHandler
from todo_scratch.bk_base.controller.controller import Controller
from todo_scratch.bk_base.http.request import Request
from todo_scratch.bk_base.http.response.http_error_response import Response404
from todo_scratch.bk_base.http.response.json_response import JSONResponse
from todo_scratch.bk_base.http.response.response import Response


class GroupChangeController(Controller):
    """グループ変更コントローラ
    ユーザの選択中のグループを変更します

    Args:
        Controller (_type_): _description_
    """

    def post(self, request: Request, user: UserEntity) -> Response:
        body = request.json

        select_group_id = body.get("group_id", None)
        if select_group_id is None:
            return Response404()

        group_handler = self._get_handler()
        group_handler.change_selected_group(
            user_id=user.user_id.value,
            select_group_id=select_group_id
        )

        return JSONResponse(
            dic=group_handler.get_selected_detail_group_info(user.user_id.value)
        )

    def _get_handler(self) -> GroupHandler:
        return GroupHandler()
