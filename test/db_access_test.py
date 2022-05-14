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
        entities: UserEntity = acceser.select_all()
        for entity in entities:
            print(entity.name.value)
        self.assertLess(0, len(entities))

    def test_db_accser_select_by_id(self):
        print("-----{0}-----".format("test_db_accser_select_by_id"))
        from todo_scratch.bk_base.db.db_accesors.db_accesor import DbAccesor
        from todo_scratch.bk_app.entities.user_entity import UserEntity
        acceser = DbAccesor(UserEntity)
        entity: UserEntity = acceser.select_by_id(2)
        print(entity.name.value)

        self.assertEqual(2, entity.user_id.value)

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

    @unittest.skip('test_db_accser_insert')
    def test_db_accser_insert(self):
        print("-----{0}-----".format("test_db_accser_insert"))
        from todo_scratch.bk_base.db.db_accesors.db_accesor import DbAccesor
        from todo_scratch.bk_app.entities.user_entity import UserEntity
        acceser = DbAccesor(UserEntity)

        user_entity_test3 = UserEntity.create_instance("test3", 10)
        user_entity_test4 = UserEntity.create_instance("test4", 11)

        effected_rows = acceser.insert_bulk([
            user_entity_test3, user_entity_test4
        ])
        self.assertLess(0, effected_rows)

    @unittest.skip('test_db_accser_update')
    def test_db_accser_update(self):
        print("-----{0}-----".format("test_db_accser_update"))
        from todo_scratch.bk_base.db.db_accesors.db_accesor import DbAccesor
        from todo_scratch.bk_app.entities.user_entity import UserEntity
        acceser = DbAccesor(UserEntity)

        # テストユーザの追加
        user_entity_test = UserEntity.create_instance("update_test_user", 99)
        acceser.insert_bulk([
            user_entity_test
        ])
        entities: UserEntity = acceser.select_by_param({
            "name": "update_test_user",
        })
        test_user: UserEntity = entities[0]
        print("select update user", test_user.name.value, test_user.age.value)

        # テストユーザの更新
        test_user.name.set_value("change_update_test_user")
        test_user.age.set_value(0)
        effect_rows = acceser.update_bulk(test_user)

        # 更新したテストユーザの更新
        update_test_user: UserEntity = acceser.select_by_id(test_user.user_id.value)
        print("select update user", update_test_user.name.value, update_test_user.age.value)
        self.assertLess(0, effect_rows)

    def test_db_accser_delete(self):
        print("-----{0}-----".format("test_db_accser_delete"))
        from todo_scratch.bk_base.db.db_accesors.db_accesor import DbAccesor
        from todo_scratch.bk_app.entities.user_entity import UserEntity
        acceser = DbAccesor(UserEntity)

        # テストユーザの追加
        user_entity_test = UserEntity.create_instance("update_test_user", 99)
        acceser.insert_bulk([
            user_entity_test
        ])
        entities: UserEntity = acceser.select_by_param({
            "name": "update_test_user",
        })
        test_user: UserEntity = entities[0]
        print("select update user", test_user.name.value, test_user.age.value)

        # テストユーザの削除
        effect_rows = acceser.delete_bulk(test_user)

        entity: UserEntity = acceser.select_by_id(test_user.user_id.value)

        print("delete entity", entity)
        self.assertLess(0, effect_rows)


if __name__ == '__main__':
    unittest.main()
