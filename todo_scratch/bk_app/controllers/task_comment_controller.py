
from typing import List
from todo_scratch.bk_app.entities.user_entity import UserEntity
from todo_scratch.bk_app.handlers.task_handler import TaskHandler
from todo_scratch.bk_base.controller.controller import Controller
from todo_scratch.bk_base.http.request import Request
from todo_scratch.bk_base.http.response.http_error_response import Response403, Response404
from todo_scratch.bk_base.http.response.json_response import JSONResponse
from todo_scratch.bk_base.http.response.response import Response


class TaskCommentController(Controller):
    """タスクコメント投稿コントローラ
    ApiUrl[/group/<int:group_id>/task/<int:task_id>/comment]のメソッドをまとめたクラスです

    Args:
        Controller (_type_): コントローラ基底クラス
    """

    def post(self, request: Request, user: UserEntity, url_path_param: List, **kwargs) -> Response:
        body = request.json
        comment = body.get('comment', None)

        if len(url_path_param) <= 1 or comment is None:
            return Response404()

        group_id = int(url_path_param[0])
        task_id = int(url_path_param[1])

        handler = self._get_handler()

        if not handler.is_join_to_group(user.user_id.value, group_id):
            return Response403()

        post_task_comment_id = handler.post_task_comment(task_id, user.user_id.value, comment)

        if post_task_comment_id <= 0:
            pass

        return JSONResponse(dic={
            "comment_id": post_task_comment_id
        })

    def _get_handler(self,) -> TaskHandler:
        return TaskHandler()
