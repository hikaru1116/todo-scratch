from todo_scratch.bk_base.validator.json_validator import JsonValidator
from todo_scratch.bk_base.validator.validator_item import DatetimeValidatorItem, IntValidatorItem, TextValidatorItem, VcharValidatorItem


class CreateTaskValidator(JsonValidator):
    """タスク新規作成用リクエストボディバリデータ

    Args:
        JsonValidator (_type_): Jsonバリデーション基底クラス
    """

    def init_validator_items(self):
        self.title = VcharValidatorItem(is_required=True)
        self.context = TextValidatorItem(is_required=True)
        self.deadline_at = DatetimeValidatorItem(is_required=True)
        self.task_status_id = IntValidatorItem(is_required=True)
