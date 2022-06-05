from typing import Dict, List
from todo_scratch.bk_app.entities.user_entity import UserEntity
from todo_scratch.bk_app.handlers.group_handler import GroupHandler
from todo_scratch.bk_app.validators.request_body_validators.create_group_validator import CreateGroupValidator
from todo_scratch.bk_app.validators.request_body_validators.update_group_validator import UpdateGroupValidator
from todo_scratch.bk_base.controller.controller import Controller
from todo_scratch.bk_base.http.request import Request
from todo_scratch.bk_base.http.response.http_error_response import Response403, Response404
from todo_scratch.bk_base.http.response.json_response import JSONResponse
from todo_scratch.bk_base.http.response.response import Response


class GroupController(Controller):
    """グループコントローラ
    ApiUrl[/group]のメソッドをまとめたクラスです

    Args:
        Controller (_type_): コントローラ基底クラス
    """

    def get(self, request: Request, user: UserEntity, url_path_param: List) -> Response:
        if len(url_path_param) <= 0:
            return Response404()

        group_id = int(url_path_param[0])

        group_handler = self._get_handler()
        if not group_handler.is_join_to_group(user.user_id.value, group_id):
            return Response403()

        return JSONResponse(dic=group_handler.get_detail_group_info(user.user_id.value, group_id))

    def post(self, request: Request, user: UserEntity, **kwargs) -> Response:
        body = request.json

        validator = CreateGroupValidator(body)
        if not validator.validate():
            return Response404()

        request_body = validator.result
        group_handler = self._get_handler()

        created_group_id = group_handler.create_group(request_body, user.user_id.value)

        group_info: Dict = group_handler.get_detail_group_info(user.user_id.value, created_group_id)

        return JSONResponse(dic=group_info)

    def put(self, request: Request, user: UserEntity, url_path_param: List) -> Response:
        if len(url_path_param) <= 0:
            return Response404()

        group_id = int(url_path_param[0])

        body = request.json
        validator = UpdateGroupValidator(body)
        if not validator.validate():
            return Response404()

        group_handler = self._get_handler()
        if not group_handler.is_host_user_in_group(user.user_id.value, group_id):
            return Response403()

        request_body = validator.result

        # グループ情報の更新
        update_group_id = group_handler.update_group_by_id(
            user_id=user.user_id.value,
            group_id=group_id,
            group_name=request_body.get("group_name"),
            description=request_body.get("description")
        )

        if request_body.get("update_users") is not None and len(request_body.get("update_users")) > 0:
            # グループのユーザ権限の更新
            group_handler.update_group_belongs(
                group_id=update_group_id,
                users=request_body.get("update_users")
            )

        if request_body.get("add_users") is not None and len(request_body.get("add_users")) > 0:
            group_handler.save_group_belong(users=request_body.get("add_users"), post_user_id=user.user_id.value, group_id=group_id)

        return JSONResponse(
            dic=group_handler.get_detail_group_info(call_user_id=user.user_id.value, group_id=update_group_id)
        )

    def _get_handler(self) -> GroupHandler:
        return GroupHandler()
