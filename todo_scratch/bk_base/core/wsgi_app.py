
import typing as t
from todo_scratch.bk_base.core.router import Router
from todo_scratch.bk_base.http.request import Request
from todo_scratch.bk_base.http.response.response import Response
from todo_scratch.bk_base.middleware.log_middleware import LogMiddleware
from todo_scratch.bk_base.middleware.middleware import Middleware, MiddlewareProcess


class WsgiApp:
    def __init__(self) -> None:
        self.router = Router()
        self.middleware = self._load_middleware()

    def wsgi_process(self, env: dict, start_response: t.Callable) -> t.Any:
        # レスポンスの取得
        request = Request(env)
        # メソッド、URLパスからコールバック、引数を取得
        callback, kwargs = self.router.match(request)
        # ミドルウェア処理
        # コールバックからレスポンスを取得
        middleware_process: MiddlewareProcess = MiddlewareProcess(
            callback, self.middleware
        )
        response: Response = middleware_process.\
            middleware_process(request, **kwargs)

        # レスポンスからステータス、ヘッダーを設定
        start_response(response.status, response.header_list)
        # レスポンスボディを返す
        return [response.body]

    def _load_middleware(self,) -> Middleware:
        return LogMiddleware()

    def __call__(self, env: dict, start_response: t.Callable) -> t.Any:
        return self.wsgi_process(env, start_response)
