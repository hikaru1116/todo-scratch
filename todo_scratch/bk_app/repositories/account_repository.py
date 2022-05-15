
from typing import List
from todo_scratch.bk_app.entities.account_entity import AccountEntity
from todo_scratch.bk_base.db.db_accesors.select_db_accesor import SelectDbAccesor


class AccountRepository:
    """ユーザアカウントに関する永続化処理をまとめたクラス
    """

    account_query = """
    SELECT
        ts_user.user_id,
        ts_user.user_name,
        ts_user.email,
        ts_group_belongs.group_id
    FROM todo_scratch.`user` as ts_user
    LEFT JOIN todo_scratch.group_belongs as ts_group_belongs
    ON ts_user.user_id = ts_group_belongs.user_id
    WHERE ts_group_belongs.user_id = %(user_id)s
    AND ts_group_belongs.is_selected = TRUE
    """

    def get_account(self, user_id: int) -> List[AccountEntity]:
        """アカウント情報の取得

        Args:
            user_id (int): ユーザID

        Returns:
            List[AccountEntity]: アカウント情報エンティティリスト
        """
        select_db_accesor = SelectDbAccesor(AccountEntity)
        return select_db_accesor.select(
            query=self.account_query,
            param={
                "user_id": user_id
            }
        )
