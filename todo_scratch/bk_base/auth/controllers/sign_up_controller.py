import re
from todo_scratch.bk_base.auth.encrypt_maneger import EncryptManeger
from todo_scratch.bk_base.auth.entities.auth_user_entity import AuthUserEntity
from todo_scratch.bk_base.auth.session_maneger import SessionManeger
from todo_scratch.bk_base.controller.controller import Controller
from todo_scratch.bk_base.db.db_accesors.db_accesor import DbAccesor
from todo_scratch.bk_base.http.request import Request
from todo_scratch.bk_base.http.response.http_error_response import Response404
from todo_scratch.bk_base.http.response.response import Response
from todo_scratch.bk_base.util.class_loader_util import get_module_by_full_route
from todo_scratch.bk_base.util.settings_util import get_member_by_settings


class SignUpController(Controller):
    """ユーザ登録コントローラ

    Args:
        Controller (_type_): コントローラ基底クラス
    """

    def post(self, request: Request, **kwargs) -> Response:
        body = request.json
        if body.get("user_name") is None or body.get("email") is None or body.get("password") is None:
            return Response404()

        user_name = body.get("user_name")
        email = body.get("email")
        password = body.get("password")

        user_entity_module = get_module_by_full_route(get_member_by_settings("AUTH_USER_ENTITY"))
        user_db_accesor: DbAccesor = DbAccesor(user_entity_module)

        if not (self._validate_user_name(user_name, user_db_accesor) and
                self._validate_email(email, user_db_accesor) and
                self._validate_password(password)):
            return Response404()

        is_two_step_verification_by_email = get_member_by_settings("IS_TWO_STEP_VERFICATION_BY_EMAIL")
        if is_two_step_verification_by_email:
            # emailによる二段階認証のための、処理を開始
            # TODO: emailによる二段階認証処理を実装
            return Response(status="200", body="二段階認証")

        # ユーザ情報を保存
        password_hashed = EncryptManeger.get_hash(password)
        user_entity = user_entity_module()
        user_entity.set_entity_values(
            user_name=user_name,
            email=email,
            password=password_hashed,
            is_admin=False
        )
        user_db_accesor.insert([user_entity])

        # セッションを作成
        insert_user_entitiy: AuthUserEntity = user_db_accesor.select_by_param(
            {"user_name": user_name, "email": email, "password": password_hashed}
        )[0]
        session_maneger = SessionManeger()
        session_code = session_maneger.generete_session(insert_user_entitiy.user_id.value)

        return Response(status="200", body=session_code)

    def _validate_user_name(self, user_name, db_accesor: DbAccesor) -> bool:
        user_entities = db_accesor.select_by_param({"user_name": user_name})
        return len(user_entities) <= 0

    def _validate_email(self, email, db_accesor: DbAccesor) -> bool:
        email_pattern = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$"
        if re.match(email_pattern, email) is None:
            return False

        user_entities = db_accesor.select_by_param({"email": email})
        return len(user_entities) <= 0

    def _validate_password(self, password) -> bool:
        return len(password) >= 8
