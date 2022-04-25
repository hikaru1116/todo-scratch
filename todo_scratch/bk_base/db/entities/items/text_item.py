

from todo_scratch.bk_base.db.entities.items.base_item import BaseItem


class TextItem(BaseItem):
    def __init__(self, value=None, length=100) -> None:
        self.value = value
        self.length = length
        super().__init__()

    def to_item(self):
        pass

    def get_value(self,):
        return self.value

    def validate(self,):
        pass
