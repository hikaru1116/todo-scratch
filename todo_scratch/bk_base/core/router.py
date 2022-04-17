import typing as t
from todo_scratch.bk_base.core.url_pattern import UrlPattern
from todo_scratch.bk_base.http.error.http_404 import Http404
from todo_scratch.bk_base.util.settings_util import get_settings
from todo_scratch.bk_base.util.class_loader_util import import_module_member_from_file_route


class Router:
    def __init__(self) -> None:
        self.urlpatterns: t.List[UrlPattern] = []
        self.load_routes()

    def load_routes(self,) -> None:
        settings = get_settings()
        self.urlpatterns = import_module_member_from_file_route('urlpatterns', settings.app_path + "." + settings.urls_path)

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
            return urlpattern.get_controller().dispatch()

        return Http404(error_detail="detail error"), {}


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
