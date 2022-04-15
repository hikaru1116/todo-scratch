
import re
import typing as t
from todo_scratch.bk_base.core.response import Response


def http404(env: dict, start_response: t.Callable) -> t.List[bytes]:
    start_response(
        '404 Not Found', [
            ('Content-type', 'text/plain; charset=utf-8')])
    return [b'404 Not Found']


def http405(env: dict, start_response: t.Callable) -> t.List[bytes]:
    start_response(
        '405 Method Not Allowed', [
            ('Content-type', 'text/plain; charset=utf-8')])
    return [b'405 Method Not Allowed']


class Router:
    def __init__(self) -> None:
        self.urls: t.List[UrlPattern] = []
        self.load_routes()

    def load_routes(self,) -> None:
        # ここでurl.pyのルーティング情報を読み込む
        urlpattern1 = UrlPattern(
            path='^/$',
            calback=lambda _: Response('Hello World')
        )
        self.urls.append(urlpattern1)

    # uripathの照合
    def match(self, method: str, path: str) -> t.Tuple[t.Callable, dict]:
        for url in self.urls:
            matchd = url.path_compiled.match(path)
            if not matchd:
                continue
            return url.calback, matchd.groupdict()

        return http404, {}


class UrlPattern:
    def __init__(self, path=None, method="GET", calback=None) -> None:
        self.path = path
        self.method = method
        self.calback = calback
        self.path_compiled = re.compile(path)


# class Router:
#     def __init__(self):
#         self.routes = []

#     def add(self, method: t.List[str], path: str, callback: t.Callable) -> None:
#         self.routes.append({
#             'method': method,
#             'path': path,
#             'path_compiled': re.compile(path),
#             'callback': callback
#         })

#     def match(self, method: str, path: str) -> t.Tuple[t.Callable, dict]:
#         error_callback = http404
#         for route in self.routes:
#             matched = route['path_compiled'].match(path)
#             if not matched:
#                 continue

#             error_callback = http405
#             url_vars = matched.groupdict()
#             if method == route['method']:
#                 return route['callback'], url_vars
#         return error_callback, {}
