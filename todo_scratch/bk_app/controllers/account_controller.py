

from todo_scratch.bk_app.entities.user_entity import UserEntity
from todo_scratch.bk_app.handlers.account_handler import AccountHandler
from todo_scratch.bk_app.validators.request_body_validators.update_account_validator import UpdateAccountValidator
from todo_scratch.bk_base.controller.controller import Controller
from todo_scratch.bk_base.http.request import Request
from todo_scratch.bk_base.http.response.http_error_response import Response404
from todo_scratch.bk_base.http.response.json_response import JSONResponse
from todo_scratch.bk_base.http.response.response import Response


class AccountController(Controller):
    """アカウントコントローラ
    ApiUrl[/account]のメソッドをまとめたクラスです

    Args:
        Controller (_type_): コントローラ基底クラス
    """

    def get(self, request: Request, user: UserEntity) -> Response:
        return JSONResponse(
            dic=self._get_handler().get_account(user.user_id.value)
        )

    def put(self, request: Request, user: UserEntity) -> Response:

        body = request.json

        validator = UpdateAccountValidator(body)
        if not validator.validate():
            return Response404()

        account_handler = self._get_handler()
        account_handler.update_account(
            user_entity=user,
            update_user_info=validator.result
        )

        return JSONResponse(
            dic=account_handler.get_account(user.user_id.value)
        )

    def _get_handler(self):
        return AccountHandler()
