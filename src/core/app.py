from src.core.router import Router
from src.core.request import Request
import os


class App:
    def __init__(self, templates=None):
        self.router = Router()
        if templates is None:
            templates = [os.path.join(os.path.abspath('.'), 'templates')]

    # ルーティングの設定
    def route(self, path=None, method='GET', callback=None):
        def decorator(callback_func):
            self.router.add(method, path, callback_func)
            return callback_func
        return decorator(callback) if callback else decorator

    # レスポンスの設定
    def __call__(self, env, start_response):
        method = env['REQUEST_METHOD'].upper()
        path = env['PATH_INFO'] or '/'
        callback, kwargs = self.router.match(method, path)

        response = callback(Request(env), **kwargs)
        start_response(response.status, response.header_list)
        return [response.body]
