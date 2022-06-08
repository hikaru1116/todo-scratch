from atom_bk_frame.db.entities.entity import Entity
from atom_bk_frame.db.entities.items import items


class GroupDetailEntity(Entity):
    """グループとグループ所属情報エンティティ

    Args:
        Entity (_type_): エンティティ基底クラス
    """

    def __init__(self) -> None:
        self.group_id = items.IntItem(is_praimary=True)
        self.group_name = items.CharItem(length=30)
        self.description = items.TextItem()
        self.auth_type = items.IntItem()
        self.user_status = items.IntItem()
        super().__init__()
