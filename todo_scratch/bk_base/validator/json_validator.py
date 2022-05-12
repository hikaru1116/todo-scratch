import json
from typing import Any
from todo_scratch.bk_base.validator.base_validator import BaseValidator


class JsonValidator(BaseValidator):

    def __init__(self, target: Any) -> None:
        super().__init__(json.loads(target))

    def validate(self):
        return super().validate()
