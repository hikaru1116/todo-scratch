
from typing import List
from todo_scratch.bk_app.handlers.task_handler import TaskHandler
from todo_scratch.bk_base.controller.controller import Controller
from todo_scratch.bk_base.http.request import Request
from todo_scratch.bk_base.http.response.http_error_response import Response404
from todo_scratch.bk_base.http.response.json_response import JSONResponse
from todo_scratch.bk_base.http.response.response import Response


class TaskDivideByStatusController(Controller):
    """タスク取得（ステータスごと）コントローラ
    ApiUrl[/group/<int:group_id>/task/divide-by-status]のメソッドをまとめたクラスです

    Args:
        Controller (_type_): コントローラ基底クラス
    """

    def get(self, request: Request, url_path_param: List, **kwargs) -> Response:

        if len(url_path_param) <= 0:
            return Response404()

        return JSONResponse(dic=self._get_handler().get_task_divide_by_task(
            group_id=int(url_path_param[0]),
        ))

    def _get_handler(self) -> TaskHandler:
        return TaskHandler()
