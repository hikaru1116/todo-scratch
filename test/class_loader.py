
import os
import unittest
from test_class import TestClass
import sys
sys.path.append('../')
print(sys.path)


class TestClassLoder(unittest.TestCase):
    """動的モジュールローダーのテストクラス
    """

    def test_class_loader(self):
        """動的モジュールからクラス生成テスト
        """
        from todo_scratch.bk_base.util.class_loader import import_module_from_file_location
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        print(BASE_DIR)
        import_cls = import_module_from_file_location('TestClass', BASE_DIR + '/test_class.py')

        # 動的モジュールからクラス生成
        import_test_class = import_cls.TestClass()
        # 静的モジュールからクラス生成
        test_class: TestClass = TestClass()

        self.assertEqual(test_class.shori(), import_test_class.shori())

    def test_load_list(self):
        """動的モジュールからリスト生成テスト
        """
        from todo_scratch.bk_base.util.class_loader import import_module_from_file_location
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        print(BASE_DIR)
        import_list_module = import_module_from_file_location('test_list', BASE_DIR + '/settings_test.py')

        # 動的モジュールからリストを生成
        import_list = import_list_module.test_list
        print(import_list)
        # リストを生成
        tmp_list = [1, 2, 3, 4, 5]
        self.assertEqual(tmp_list, import_list)


if __name__ == '__main__':

    print("start test")
    unittest.main()
