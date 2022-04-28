import os
# import mysql.connector as mysql
import unittest
import sys
# importモジュールのディレクトリを設定
sys.path.append('../')


class TestTemplate(unittest.TestCase):
    """DB関連の処理テスト

    Args:
        unittest (_type_): ユニットテスト
    """

    @classmethod
    def setUpClass(cls):
        os.environ.setdefault('SETTINGS_PATH', 'todo_scratch.bk_app.settings')

    def test_select_acceser(self,):
        from todo_scratch.bk_app.entities.user_entity import UserEntity
        from todo_scratch.bk_base.db.db_accesors.select_db_accesor import SelectDbAccesor
        select_query_tuple = "select * from todo_scratch.`user` where `name` = %s"
        select_query_dict = "select * from todo_scratch.`user` where `name` = %(name)s"

        accesor = SelectDbAccesor(UserEntity)
        entities: UserEntity = accesor.select(select_query_tuple, param=('miyuki',))
        self.assertLess(0, len(entities))
        entities = accesor.select(select_query_dict, param={"name": "hikaru", })
        self.assertLess(0, len(entities))

    def test_db_accser(self):
        pass


if __name__ == '__main__':
    unittest.main()
