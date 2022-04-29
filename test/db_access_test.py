import os
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
        print("-----{0}-----".format("test_select_acceser"))
        from todo_scratch.bk_app.entities.user_entity import UserEntity
        from todo_scratch.bk_base.db.db_accesors.select_db_accesor import SelectDbAccesor
        select_query_tuple = "select * from todo_scratch.`user` where `name` = %s"
        select_query_dict = "select * from todo_scratch.`user` where `name` = %(name)s"

        accesor = SelectDbAccesor(UserEntity)
        entities: UserEntity = accesor.select(select_query_tuple, param=('miyuki',))
        self.assertLess(0, len(entities))
        entities = accesor.select(select_query_dict, param={"name": "hikaru", })
        self.assertLess(0, len(entities))

    def test_db_accser_select(self):
        print("-----{0}-----".format("test_db_accser_select"))
        from todo_scratch.bk_base.db.db_accesors.db_accesor import DbAccesor
        from todo_scratch.bk_app.entities.user_entity import UserEntity
        acceser = DbAccesor(UserEntity)
        entities: UserEntity = acceser.select()
        for entity in entities:
            print(entity.name.value)
        self.assertLess(0, len(entities))

    def test_db_accser_select_by_id(self):
        print("-----{0}-----".format("test_db_accser_select_by_id"))
        from todo_scratch.bk_base.db.db_accesors.db_accesor import DbAccesor
        from todo_scratch.bk_app.entities.user_entity import UserEntity
        acceser = DbAccesor(UserEntity)
        entities: UserEntity = acceser.select_by_id(2)
        for entity in entities:
            print(entity.name.value)
        self.assertLess(0, len(entities))

    def test_db_accser_select_by_param(self):
        print("-----{0}-----".format("test_db_accser_select_by_param"))
        from todo_scratch.bk_base.db.db_accesors.db_accesor import DbAccesor
        from todo_scratch.bk_app.entities.user_entity import UserEntity
        acceser = DbAccesor(UserEntity)
        entities: UserEntity = acceser.select_by_param({
            "name": "kotaro",
        })
        for entity in entities:
            print(entity.name.value)
        self.assertLess(0, len(entities))

    def test_db_accser_insert(self):
        print("-----{0}-----".format("test_db_accser_insert"))
        from todo_scratch.bk_base.db.db_accesors.db_accesor import DbAccesor
        from todo_scratch.bk_app.entities.user_entity import UserEntity
        acceser = DbAccesor(UserEntity)

        user_entity_test3 = UserEntity.create_instance("test3", 10)
        user_entity_test4 = UserEntity.create_instance("test4", 11)

        effected_rows = acceser.insert([
            user_entity_test3, user_entity_test4
        ])
        self.assertLess(0, effected_rows)


if __name__ == '__main__':
    unittest.main()
