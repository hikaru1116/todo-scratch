from todo_scratch.bk_base.validator.json_validator import JsonValidator
from todo_scratch.bk_base.validator.validator_item import ListValidatorItem, VcharValidatorItem


class CreateGroupValidator(JsonValidator):
    """ユーザ新規作成用リクエストボディバリデータ

    Args:
        JsonValidator (_type_): Jsonバリデーション基底クラス
    """

    def init_validator_items(self):
        self.group_name = VcharValidatorItem(is_required=True)
        self.description = VcharValidatorItem(is_required=True)
        self.invite_users = ListValidatorItem(InviteUsersValidator)


class InviteUsersValidator(JsonValidator):
    def init_validator_items(self) -> None:
        self.identifier = VcharValidatorItem(is_required=True)
