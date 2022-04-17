from todo_scratch.bk_base.controller.controller import Controller
from typing import Dict, Tuple, Callable
from todo_scratch.bk_base.http.request import Request

from todo_scratch.bk_base.http.response import Response


class BaseController(Controller):

    def __init__(self) -> None:
        super().__init__()
        self.http_method = ["GET", "POST"]

    def get_callback(self, path=None, method="GET") -> Tuple[Callable, Dict]:

        if method not in self.http_method:
            pass

        if "GET" == method:
            return self.get, {}
        else:
            return self.post, {}

    def get(self, request: Request,) -> Response:
        raise NotImplementedError

    def post(self, request: Request) -> Response:
        raise NotImplementedError
