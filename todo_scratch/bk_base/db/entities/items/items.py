from todo_scratch.bk_base.db.entities.items.base_item import BaseItem


class CharItem(BaseItem):
    def __init__(self, length=0, is_praimary=False, is_insert_require=True) -> None:
        self.length = length
        super().__init__(is_praimary, is_insert_require)


class VcharItem(BaseItem):
    pass


class TextItem(BaseItem):
    pass


class IntItem(BaseItem):
    pass


class BoolItem(BaseItem):
    pass


class DatetimeItem(BaseItem):
    pass
