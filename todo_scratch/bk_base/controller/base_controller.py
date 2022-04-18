from todo_scratch.bk_base.controller.controller import Controller
from typing import Dict, Tuple, Callable
from todo_scratch.bk_base.http.http_error import get_405_callback
from todo_scratch.bk_base.http.request import Request
from todo_scratch.bk_base.http.response.response import Response


class BaseController(Controller):

    http_method = ["GET", "POST"]

    def dispatch(self, method="GET") -> Tuple[Callable, Dict]:

        if method not in self.http_method:
            return get_405_callback()

        if "GET" == method:
            return self.get, {}
        else:
            return self.post, {}

    def get(self, request: Request, **kwargs) -> Response:
        raise NotImplementedError

    def post(self, request: Request, **kwargs) -> Response:
        raise NotImplementedError
