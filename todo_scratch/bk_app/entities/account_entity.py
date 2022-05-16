
from todo_scratch.bk_base.db.entities.entity import Entity
from todo_scratch.bk_base.db.entities.items import items


class AccountEntity(Entity):
    """アカウント情報エンティティ

    Args:
        Entity (_type_): エンティティ基底クラス
    """

    def __init__(self) -> None:
        self.user_id = items.IntItem(is_praimary=True)
        self.user_name = items.CharItem(length=30)
        self.email = items.CharItem(length=100)
        super().__init__()
