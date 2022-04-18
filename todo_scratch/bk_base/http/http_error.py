from typing import Callable, Dict, Tuple
from todo_scratch.bk_base.http.request import Request
from todo_scratch.bk_base.http.response.response import Response


class Response404(Response):
    default_status = "404"


class Response405(Response):
    default_status = "405"


def get_404_callback() -> Tuple[Callable, Dict]:
    def error_callback(request: Request, **kwargs) -> Response:
        return Response404(body="not found")

    return error_callback, {}


def get_405_callback() -> Tuple[Callable, Dict]:
    def error_callback(request: Request, **kwargs) -> Response:
        return Response405(body="not allow method")

    return error_callback, {}
