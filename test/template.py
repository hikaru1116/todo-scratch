import unittest
import sys
# importモジュールのディレクトリを設定
sys.path.append('../')


# テストコードテンプレート
class TestTemplate(unittest.TestCase):
    def test_class_loader(self):
        num = 3

        self.assertEqual(num, 3)


if __name__ == '__main__':
    unittest.main()
