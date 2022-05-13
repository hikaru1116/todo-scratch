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
        data1 = {
            "group_name": "group_name_test",
            "description": "description text"
        }
        create_group_validator1 = CreateGroupValidator(json.dumps(data1).encode())
        validation_result = create_group_validator1.validate()
        self.assertTrue((validation_result) and len(create_group_validator1.result) > 0)

        data2 = {
            "description": "description text"
        }
        create_group_validator2 = CreateGroupValidator(json.dumps(data2).encode())
        validation_result = create_group_validator2.validate()
        self.assertTrue((not validation_result) and len(create_group_validator2.result) <= 0)


if __name__ == '__main__':
    unittest.main()
