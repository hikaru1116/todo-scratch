from typing import Dict
from todo_scratch.bk_app.entities.user_entity import UserEntity

from todo_scratch.bk_app.repositories.account_repository import AccountRepository


class AccountHandler:
    """AccountControllerのハンドラクラス
    """

    def __init__(self) -> None:
        self.account_repository = AccountRepository()

    def get_account(self, user_id: int) -> Dict:
        """アカウント情報の取得

        Args:
            user_id (int): ユーザID

        Returns:
            Dict: アカウント情報
        """
        account_entities = self.account_repository.get_account(user_id=user_id)

        if len(account_entities) <= 0:
            return {}

        return account_entities[0].to_dict()

    def update_account(self, user_entity: UserEntity, update_user_info: Dict) -> None:
        """アカウント（ユーザ）情報の更新

        Args:
            user_entity (UserEntity): ユーザエンティティ
            update_user_info (Dict): 変更するユーザ情報
        """
        user_entity.user_name.set_value(update_user_info.get("user_name"))
        user_entity.email.set_value(update_user_info.get("email"))

        self.account_repository.update_account(user_entity)
