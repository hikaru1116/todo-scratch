from todo_scratch.bk_app.handlers.group_handler import GroupHandler
from todo_scratch.bk_base.controller.controller import Controller
from todo_scratch.bk_base.http.request import Request
from todo_scratch.bk_base.http.response.http_error_response import Response404
from todo_scratch.bk_base.http.response.response import Response
# from todo_scratch.bk_base.util.log.log_util import get_logger


class GroupController(Controller):

    def post(self, request: Request, **kwargs) -> Response:
        body = request.json
        if body.get("group_name") is None or\
                body.get("description") is None:
            return Response404()

        group_name = body.get("group_name")
        description = body.get("description")
        invite_user = body.get("invite_users")

        print(group_name, description, invite_user)
        # handler = self.get_handler()
        return Response()

    def get_handler(self):
        return GroupHandler()
