import typing as t


class TestMiddleware:
    def __init__(self, app) -> None:
        self.app = app

    def __call__(self, env: dict, start_response: t.Callable) -> t.Any:
        print("Fire TestMiddleWare!!")
        return self.app(env, start_response)
