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

    def test_db_access(self,):
        from todo_scratch.bk_app.entities.user_entity import UserEntity
        from todo_scratch.bk_base.db.db_accesors.select_db_accesor import SelectDbAccesor

        accesor = SelectDbAccesor(UserEntity)
        entities: UserEntity = accesor.select(
            "select * from todo_scratch.`user`"
        )
        for entity in entities:
            print(entity.name.value, entity.age.value, entity.context.value)
        self.assertEqual(1, 1)

    # db_config = {
    #     'host': '192.168.64.3',
    #     'port': '3306',
    #     'user': 'admin',
    #     'password': 'P@ssw0rd',
    #     'database': 'todo_scratch'
    # }

    # def test_db(self):

        # from todo_scratch.bk_base.db.db_drivers.db_driver import DbDriver
        # from todo_scratch.bk_base.db.db_drivers.db_driver_maneger import DbDriverManeger

        # db_driver: DbDriver = DbDriverManeger.get_db_driver('mysql')

        # db_driver.connect()
        # print(db_driver.__class__.__name__)
        # print('connect ', db_driver.is_connect())
        # result = db_driver.query("select * from todo_scratch.`user`")
        # print(result)
        # db_driver.disconnect()

        # accesor = QueryDbAccesor(UserEntity)
        # entity = accesor.select(
        #     "select * from todo_scratch.`user`"
        # )
        # print(entity)
        # self.assertEqual(1, 1)

    # def test_class_loader(self):
    #     query_select = "select * from todo_scratch.`user`"
    #     conn = mysql.connect(**self.db_config)
    #     cur = conn.cursor()
    #     cur.execute(query_select)

    #     rows = cur.fetchall()
    #     # print(rows)
    #     # print(type(rows), type(rows[0]))
    #     cur.close()
    #     conn.close()
    #     self.assertEqual(rows[0][1], 'hikaru')

    #     query_insert = "insert into user(name, age, content) VALUES (%s,%s,%s)"
    #     conn = mysql.connect(**self.db_config)

    #     # 自動コミット制御
    #     conn.autocommit = False
    #     cur = conn.cursor()
    #     try:
    #         cur.execute(query_insert, ['test7', '20', 'テストデータを挿入します'])
    #         conn.commit()
    #     except Exception as e:
    #         print(e.args)
    #         # ロールバック
    #         conn.rollback()
    #         cur.close()
    #         conn.close()
    #         raise Exception

    #     cur.execute(query_select)
    #     rows = cur.fetchall()
    #     self.assertEqual(rows[-1][1], 'test7')
    #     cur.close()
    #     conn.close()


if __name__ == '__main__':
    unittest.main()
