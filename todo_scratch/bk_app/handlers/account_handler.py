from typing import Dict

from todo_scratch.bk_app.repositories.account_repository import AccountRepository


class AccountHandler:

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
