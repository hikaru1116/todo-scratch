import typing as t
from todo_scratch.bk_base.core.url_pattern import UrlPattern
from todo_scratch.bk_base.http.http_error import get_404_callback
from todo_scratch.bk_base.http.request import Request
from todo_scratch.bk_base.util.settings_util import get_module_path_by_settings
from todo_scratch.bk_base.util.class_loader_util import import_module_member_from_file_route


class Router:

    URL_PATTERN = "urlpatterns"

    def __init__(self) -> None:
        self.urlpatterns: t.List[UrlPattern] = []
        self.load_routes()

    def load_routes(self,) -> None:
        self.urlpatterns = import_module_member_from_file_route(
            self.URL_PATTERN,
            get_module_path_by_settings("URLS_PATH")
        )

    def match(self, request: Request) -> t.Tuple[t.Callable, dict]:
        """Urlの照合

        Args:
            method (str): メソッド
            path (str): Urlパス

        Returns:
            t.Tuple[t.Callable, dict]: wsgiレスポンスコールバック
        """
        for urlpattern in self.urlpatterns:
            matchd = urlpattern.get_path_compiled().match(request.path)
            if not matchd:
                continue
            return urlpattern.get_controller().dispatch(method=request.method)

        return get_404_callback()
