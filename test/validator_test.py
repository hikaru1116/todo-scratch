import json
import unittest
import sys


# importモジュールのディレクトリを設定
sys.path.append('../')


class ValidatorTest(unittest.TestCase):
    """バリデーション処理テスト

    Args:
        unittest (_type_): ユニットテスト基底クラス
    """

    def test_json_validator(self):

        from todo_scratch.bk_app.validators.request_body_validators.create_group_validator import CreateGroupValidator
        data = {
            "group_name": "test_group",
            "description": "description text"
        }

        create_group_validator = CreateGroupValidator(json.dumps(data).encode())

        if not create_group_validator.validate():
            print("fail validate")

        else:
            print("success validate")

        self.assertEqual(create_group_validator.result.get("group_name"), data.get("group_name"))


if __name__ == '__main__':
    unittest.main()
