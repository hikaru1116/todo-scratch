
import typing as t
from todo_scratch.bk_base.core.request import Request
from todo_scratch.bk_base.core.router import Router


class App:
    def __init__(self) -> None:
        self.middleware: t.List = []
        self.router = Router()

    def response(self, env: dict, start_response: t.Callable) -> t.Any:
        method = env['REQUEST_METHOD'].upper()
        path = env['PATH_INFO'] or '/'
        callback, kwargs = self.router.match(method, path)
        response = callback(Request(env), **kwargs)
        start_response(response.status, response.header_list)
        return [response.body]
