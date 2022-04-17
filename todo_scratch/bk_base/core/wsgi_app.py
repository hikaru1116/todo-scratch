
import typing as t
from todo_scratch.bk_base.core.app import App


class WsgiApp:
    def __init__(self) -> None:
        self.app = App()

    def __call__(self, env: dict, start_response: t.Callable) -> t.Any:
        return self.app(env, start_response)
