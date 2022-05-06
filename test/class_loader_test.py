
import os
from typing import List
import unittest
import sys
sys.path.append('../')
print(sys.path)


class TestClass:

    def shori(self):
        return "shori"


class TestClassLoder(unittest.TestCase):
    """動的モジュールローダーのテストクラス
    """

    @classmethod
    def setUpClass(cls):
        os.environ.setdefault('SETTINGS_PATH', 'todo_scratch.bk_app.settings')

    def test_class_loader(self):
        """動的モジュールからクラス生成テスト
        """
        print("-----{0}-----".format("test_class_loader"))
        from todo_scratch.bk_base.util.class_loader_util import get_module_by_file_path
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        print(BASE_DIR)
        import_cls = get_module_by_file_path('TestClass', BASE_DIR + '/class_loader_test.py')

        # 動的モジュールからクラス生成
        import_test_class = import_cls.TestClass()
        # 静的モジュールからクラス生成
        test_class: TestClass = TestClass()

        self.assertEqual(test_class.shori(), import_test_class.shori())

    def test_route_loder(self):
        print("-----{0}-----".format("test_route_loder"))
        from todo_scratch.bk_base.util.class_loader_util import get_module_by_route

        urlpatterns = get_module_by_route('urlpatterns', 'todo_scratch.bk_app.urls')

        print(urlpatterns)
        self.assertEqual(3, 3)

    def test_import_module_by_route(self):
        print("-----{0}-----".format("test_import_module_by_route"))
        from todo_scratch.bk_base.util.class_loader_util import get_module_by_full_route
        from todo_scratch.bk_base.util.settings_util import get_member_by_settings

        middlewares: List[str] = get_member_by_settings("MIDDLEWARES")
        for middleware in middlewares:
            module = get_module_by_full_route(middleware)
            print(module)

        self.assertEqual(3, 3)


if __name__ == '__main__':

    print("start test")
    unittest.main()
