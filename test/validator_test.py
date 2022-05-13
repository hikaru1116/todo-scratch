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
            "description": "description text",
            "invire_users": [
                {"identify": "test1"},
                {"identify": "test2"},
                {"identify": "test3"},
                {"identif": "test4"}
            ]
        }
        create_group_validator1 = CreateGroupValidator(data1)
        validation_result = create_group_validator1.validate()
        print(create_group_validator1.result, type(create_group_validator1.result))
        self.assertTrue((validation_result) and len(create_group_validator1.result) > 0)

        data2 = {
            "description": "description text"
        }
        create_group_validator2 = CreateGroupValidator(data2)
        validation_result = create_group_validator2.validate()
        self.assertTrue((not validation_result) and len(create_group_validator2.result) <= 0)


if __name__ == '__main__':
    unittest.main()
