
import re
import typing as t
from todo_scratch.bk_base.core.url_pattern import UrlPattern
from todo_scratch.bk_app.urls import urlpatterns


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
        self.urlpatterns: t.List[UrlPattern] = []
        self.load_routes()

    def load_routes(self,) -> None:
        self.urlpatterns = urlpatterns

    def match(self, method: str, path: str) -> t.Tuple[t.Callable, dict]:
        """Urlの照合

        Args:
            method (str): メソッド
            path (str): Urlパス

        Returns:
            t.Tuple[t.Callable, dict]: wsgiレスポンスコールバック
        """
        for urlpattern in self.urlpatterns:
            matchd = urlpattern.get_path_compiled().match(path)
            if not matchd:
                continue
            print("match callback")
            return urlpattern.get_controller().get_callback()

        return http404, {}


class UrlPattern1:
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
