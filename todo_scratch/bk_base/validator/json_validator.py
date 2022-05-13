import json
from typing import Any
from todo_scratch.bk_base.validator.base_validator import BaseValidator
from todo_scratch.bk_base.validator.validator_item import ValidatorItem


class JsonValidator(BaseValidator):
    """Jsonバリデーションクラス

    Args:
        BaseValidator (_type_): バリデーション基底クラス
    """

    def __init__(self, target: Any) -> None:
        super().__init__(json.loads(target))

    def validate(self):
        for key, value in self.__dict__.items():
            if not isinstance(value, ValidatorItem):
                continue

            validator: ValidatorItem = value
            target_item = self.target.get(key)

            if target_item is None:
                continue

            if not validator.validate(target_item):
                return False

        return True

    @property
    def result(self):
        for key, value in self.__dict__.items():
            if not isinstance(value, ValidatorItem):
                continue

            validator: ValidatorItem = value
            target_item = self.target.get(key)

            if target_item is None:
                continue

            print(target_item)
            self._result[key] = validator.convert(target_item)

        return self._result
