
from abc import ABC, abstractclassmethod
# from typing import Callable, Dict, Tuple
from todo_scratch.bk_base.http.request import Request
from todo_scratch.bk_base.http.response import Response


class HttpError(ABC):

    @abstractclassmethod
    def __call__(self, request: Request) -> Response:
        raise NotImplementedError
