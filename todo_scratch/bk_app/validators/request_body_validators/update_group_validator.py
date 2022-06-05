from todo_scratch.bk_base.validator.json_validator import JsonValidator
from todo_scratch.bk_base.validator.validator_item import IntValidatorItem, ListValidatorItem, VcharValidatorItem


class UpdateGroupValidator(JsonValidator):
    """ユーザ更新用リクエストボディバリデータ

    Args:
        JsonValidator (_type_): Jsonバリデーション基底クラス
    """

    def init_validator_items(self):
        self.group_name = VcharValidatorItem(is_required=True)
        self.description = VcharValidatorItem(is_required=True)
        self.update_users = ListValidatorItem(UpDateAuthTypeUsers)
        self.add_users = ListValidatorItem(AddUsers)


class UpDateAuthTypeUsers(JsonValidator):
    def init_validator_items(self) -> None:
        self.user_id = IntValidatorItem(is_required=True)
        self.auth_type = IntValidatorItem(is_required=True)


class AddUsers(JsonValidator):
    def init_validator_items(self) -> None:
        self.identifier = VcharValidatorItem(is_required=True)
