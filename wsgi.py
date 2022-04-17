import typing as t
from todo_scratch.bk_base.core.app import App


def get_wsgi():
    return WsgiApplication()


class WsgiApplication:
    def __init__(self) -> None:
        print("init WsgiHandler")
        self.app = App()

    def __call__(self, env: dict, start_response: t.Callable) -> t.Any:
        return self.app.dispatch(env, start_response)
