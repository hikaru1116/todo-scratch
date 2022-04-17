
import typing as t
from todo_scratch.bk_base.http.request import Request
from todo_scratch.bk_base.core.router import Router


class App:
    def __init__(self) -> None:
        self.middleware: t.List = []
        self.router = Router()

    def __call__(self, env: dict, start_response: t.Callable) -> t.Any:
        # メソッド取得
        method = env['REQUEST_METHOD'].upper()
        # Urlパスを取得
        path = env['PATH_INFO'] or '/'
        # メソッド、URLパスからコールバックを取得
        # ここで認証やらの情報の取得とかもしていきたい(kwrgs)、そして返すCallBackのみ返したい
        callback, kwargs = self.router.match(method, path)
        # コールバックからレスポンスを取得
        response = callback(Request(env), **kwargs)
        # レスポンスからステータス、ヘッダーを設定
        start_response(response.status, response.header_list)
        # レスポンスボディを返す
        return [response.body]
