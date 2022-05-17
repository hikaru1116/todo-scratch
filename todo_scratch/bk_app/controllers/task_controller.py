
from typing import List
from todo_scratch.bk_app.entities.user_entity import UserEntity
from todo_scratch.bk_app.handlers.task_handler import TaskHandler
from todo_scratch.bk_app.validators.request_body_validators.task_data_validator import TaskDataValidator
from todo_scratch.bk_base.controller.controller import Controller
from todo_scratch.bk_base.http.request import Request
from todo_scratch.bk_base.http.response.http_error_response import Response404
from todo_scratch.bk_base.http.response.response import Response


class TaskController(Controller):
    """タスクコントローラ
    ApiUrl[/group/<int:group_id>/task]のメソッドをまとめたクラスです

    Args:
        Controller (_type_): コントローラ基底クラス
    """

    def post(self, request: Request, user: UserEntity, url_path_param: List) -> Response:
        if len(url_path_param) <= 0:
            return Response404()

        group_id = int(url_path_param[0])
        body = request.json

        validator = TaskDataValidator(body)
        if not validator.validate():
            return Response404()

        handler = self._get_handler()

        if not handler.is_join_to_group(user.user_id.value, group_id):
            return Response404()

        if not handler.create_task(group_id, user.user_id.value, validator.result):
            return Response404()

        return Response()

    def put(self, request: Request, user: UserEntity, url_path_param: List, **kwargs) -> Response:
        if len(url_path_param) <= 1:
            return Response404()

        group_id = int(url_path_param[0])
        task_id = int(url_path_param[1])

        body = request.json

        validator = TaskDataValidator(body)
        if not validator.validate():
            return Response404()

        if not self._get_handler().update_task(task_id, group_id, user, validator.result):
            return Response404()

        return Response()

    def delete(self, request: Request, user: UserEntity, url_path_param: List, **kwargs) -> Response:
        if len(url_path_param) <= 1:
            return Response404()

        group_id = int(url_path_param[0])
        task_id = int(url_path_param[1])

        if not self._get_handler().delete_task(task_id, group_id, user.user_id.value):
            return Response404()

        return Response()

    def _get_handler(self) -> TaskHandler:
        return TaskHandler()
