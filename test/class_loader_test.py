
import os
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

    def test_class_loader(self):
        """動的モジュールからクラス生成テスト
        """
        from todo_scratch.bk_base.util.class_loader_util import import_module_from_file_location
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        print(BASE_DIR)
        import_cls = import_module_from_file_location('TestClass', BASE_DIR + '/class_loader_test.py')

        # 動的モジュールからクラス生成
        import_test_class = import_cls.TestClass()
        # 静的モジュールからクラス生成
        test_class: TestClass = TestClass()

        self.assertEqual(test_class.shori(), import_test_class.shori())

    def test_route_loder(self):
        from todo_scratch.bk_base.util.class_loader_util import import_module_member_from_file_route

        urlpatterns = import_module_member_from_file_route('urlpatterns', 'todo_scratch.bk_app.urls')

        print(urlpatterns)
        self.assertEqual(3, 3)


if __name__ == '__main__':

    print("start test")
    unittest.main()
