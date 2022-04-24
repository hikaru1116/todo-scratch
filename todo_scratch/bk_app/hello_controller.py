from todo_scratch.bk_base.controller.controller import Controller
from todo_scratch.bk_base.http.request import Request
from todo_scratch.bk_base.http.response.response import Response
from todo_scratch.bk_base.util.log.log_util import get_logger


class HelloController(Controller):
    """HelloWorld

    Args:
        Controller (_type_): _description_
    """

    def __init__(self) -> None:
        super().__init__()

    def get(self, request: Request, **kwargs) -> Response:
        get_logger('main').info('hello world get')
        return Response('Hello World GET\n')

    def post(self, request: Request, **kwargs) -> Response:
        get_logger('main').info('hello world post')
        return Response('Hello, World POST\n')
