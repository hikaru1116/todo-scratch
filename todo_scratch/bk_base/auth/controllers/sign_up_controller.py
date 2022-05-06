from todo_scratch.bk_base.controller.controller import Controller
from todo_scratch.bk_base.http.request import Request
from todo_scratch.bk_base.http.response.response import Response


class SignUpController(Controller):

    def post(self, request: Request, **kwargs) -> Response:

        return super().post(request, **kwargs)
