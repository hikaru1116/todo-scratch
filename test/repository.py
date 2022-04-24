import unittest
import sys
# importモジュールのディレクトリを設定
sys.path.append('../')


class TestTemplate(unittest.TestCase):
    """DB関連の処理テスト

    Args:
        unittest (_type_): ユニットテスト
    """

    def test_class_loader(self):

        self.assertEqual('1', 1)


if __name__ == '__main__':
    unittest.main()
