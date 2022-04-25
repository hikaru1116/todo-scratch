
from todo_scratch.bk_base.db.entities.items.base_item import BaseItem


class IntItem(BaseItem):

    def __init__(self, value) -> None:
        self.value = value
        super().__init__()

    def to_item(self):
        pass

    def get_value(self,):
        return self.value

    def validate(self,):
        pass
