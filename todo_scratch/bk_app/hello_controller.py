
from todo_scratch.bk_base.controller.base_controller import BaseController
from todo_scratch.bk_base.http.request import Request
from todo_scratch.bk_base.http.response import Response


class HelloController(BaseController):
    """HelloWorld

    Args:
        BaseController (_type_): _description_
    """

    def get(self, request: Request) -> Response:
        return Response('Hello World \n')
