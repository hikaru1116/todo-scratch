
import typing as t
from todo_scratch.bk_base.core.router import Router
from todo_scratch.bk_base.http.request import Request


class WsgiApp:
    def __init__(self) -> None:
        self.router = Router()
        self.middleware: t.List = []

    def wsgi_process(self, env: dict, start_response: t.Callable) -> t.Any:
        # レスポンスの取得
        request = Request(env)
        # メソッド、URLパスからコールバックを取得
        callback, kwargs = self.router.match(request)
        # コールバックからレスポンスを取得
        response = callback(request, **kwargs)
        # レスポンスからステータス、ヘッダーを設定
        start_response(response.status, response.header_list)
        # レスポンスボディを返す
        return [response.body]

    def load_middleware(self,) -> None:
        pass

    def __call__(self, env: dict, start_response: t.Callable) -> t.Any:
        return self.wsgi_process(env, start_response)

    