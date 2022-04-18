
from todo_scratch.bk_base.controller.base_controller import BaseController
from todo_scratch.bk_base.http.request import Request
from todo_scratch.bk_base.http.response.response import Response


class HelloController(BaseController):
    """HelloWorld

    Args:
        BaseController (_type_): _description_
    """

    def get(self, request: Request, **kwargs) -> Response:
        return Response('Hello World GET\n')

    def post(self, request: Request, **kwargs) -> Response:
        return Response('Hello, World POST\n')
