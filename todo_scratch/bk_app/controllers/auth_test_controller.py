

from urllib.request import Request
from todo_scratch.bk_base.auth.controllers.auth_mixin import AuthMixin
from todo_scratch.bk_base.controller.controller import Controller
from todo_scratch.bk_base.http.response.response import Response


class AuthorizedController(AuthMixin, Controller):
    """認証済みテスト用コントローラ

    Args:
        AuthMixin (_type_): 認証・認可処理Mixin
        Controller (_type_): コントローラ基底クラス
    """

    def get(self, request: Request, user) -> Response:
        print('AuthorizedController')
        print(user, user.user_name.value)
        return super().get(request)


class ForbddenController(AuthMixin, Controller):
    """管理者のみ発火可能なテスト用コントローラ

    Args:
        AuthMixin (_type_): 認証・認可処理Mixin
        Controller (_type_): コントローラ基底クラス

    """
    is_admin = True

    def get(self, request: Request, user) -> Response:
        print('ForbddenController')
        print(user, user.user_name.value)
        return super().get(request)
