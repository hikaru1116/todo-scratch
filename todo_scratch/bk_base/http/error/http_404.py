

from todo_scratch.bk_base.http.error.http_error import HttpError
# from typing import Callable, Dict, Tuple
from todo_scratch.bk_base.http.request import Request
from todo_scratch.bk_base.http.response import Response


class Http404(HttpError):

    def __init__(self, error_detail="") -> None:
        super().__init__()
        self.error_detail = error_detail

    def __call__(self, request: Request) -> Response:
        error_response = Response(body="Not Found Error:{}".format(
            self.error_detail
        ), status="404")

        return error_response
