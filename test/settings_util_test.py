import unittest
import os
import sys
# importモジュールのディレクトリを設定
sys.path.append('../')


class TestTemplate(unittest.TestCase):
    """設定ファイル取得Utilファイルテスト

    Args:
        unittest (_type_): unittest
    """
    @classmethod
    def setUpClass(cls):
        os.environ.setdefault('SETTINGS_PATH', 'todo_scratch.bk_app.settings')

    def test_class_loader(self):
        from todo_scratch.bk_base.util.settings_util import get_settings
        settings = get_settings()
        print(settings.APP_PATH)

        self.assertEqual(settings.APP_PATH, 'todo_scratch.bk_app')


if __name__ == '__main__':
    unittest.main()
