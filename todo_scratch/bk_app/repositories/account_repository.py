
from typing import List
from todo_scratch.bk_app.entities.account_entity import AccountEntity
from todo_scratch.bk_app.entities.user_entity import UserEntity
from todo_scratch.bk_base.db.db_accesors.db_accesor import DbAccesor
from todo_scratch.bk_base.db.db_accesors.select_db_accesor import SelectDbAccesor


class AccountRepository:
    """ユーザアカウントに関する永続化処理をまとめたクラス
    """

    account_query = """
    SELECT
        ts_user.user_id,
        ts_user.user_name,
        ts_user.email
    FROM todo_scratch.`user` as ts_user
    WHERE ts_user.user_id = %(user_id)s
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

    def update_account(self, user_entity: UserEntity) -> int:
        """アカウント（ユーザ）の更新

        Args:
            user_entity (UserEntity): ユーザエンティティ

        Returns:
            int: 更新したユーザのID
        """
        db_accesor = DbAccesor(UserEntity)
        return db_accesor.update(user_entity)
