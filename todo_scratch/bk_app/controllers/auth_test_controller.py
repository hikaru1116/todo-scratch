from urllib.request import Request
from atom_bk_frame.controller.auth_mixin import AuthMixin
from atom_bk_frame.controller.controller import Controller
from atom_bk_frame.http.response.response import Response


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
