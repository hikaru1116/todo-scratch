
from typing import List
from todo_scratch.bk_app.entities.user_entity import UserEntity
from todo_scratch.bk_app.handlers.task_handler import TaskHandler
from todo_scratch.bk_base.controller.controller import Controller
from todo_scratch.bk_base.http.request import Request
from todo_scratch.bk_base.http.response.http_error_response import Response403, Response404
from todo_scratch.bk_base.http.response.response import Response


class TaskChangeStatusController(Controller):
    """タスク状態変更コントローラ
    ApiUrl[/group/<int:group_id>/task/<int:task_id>/change-status]のメソッドをまとめたクラスです

    Args:
        Controller (_type_): コントローラ基底クラス
    """

    def put(self, request: Request, user: UserEntity, url_path_param: List, **kwargs) -> Response:

        body = request.json
        task_status_id = body.get('task_status_id', None)

        if len(url_path_param) <= 1 or task_status_id is None:
            return Response404()

        group_id = int(url_path_param[0])
        task_id = int(url_path_param[1])

        handler = self._get_handler()
        if not handler.is_join_to_group(user.user_id.value, group_id):
            return Response403()

        if not handler.change_task_status(task_id, group_id, user, task_status_id):
            return Response404()

        return Response()

    def _get_handler(self,):
        return TaskHandler()
