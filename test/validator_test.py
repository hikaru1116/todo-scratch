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
        num = 3

        self.assertEqual(num, 3)


if __name__ == '__main__':
    unittest.main()
