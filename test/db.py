import mysql.connector as mysql
import unittest
import sys
# importモジュールのディレクトリを設定
sys.path.append('../')


class TestTemplate(unittest.TestCase):
    """DB関連の処理テスト

    Args:
        unittest (_type_): ユニットテスト
    """

    db_config = {
        'host': '192.168.64.3',
        'port': '3306',
        'user': 'admin',
        'password': 'P@ssw0rd',
        'database': 'todo_scratch'
    }

    def test_class_loader(self):
        query_select = "select * from todo_scratch.`user`"
        conn = mysql.connect(**self.db_config)
        cur = conn.cursor()
        cur.execute(query_select)

        rows = cur.fetchall()
        print(rows)
        print(type(rows), type(rows[0]))
        cur.close()
        conn.close()
        self.assertEqual(rows[0][1], 'hikaru')

        query_insert = "insert into user(name, age, content) VALUES (%s,%s,%s)"
        conn = mysql.connect(**self.db_config)

        # 自動コミット制御
        conn.autocommit = False
        cur = conn.cursor()
        try:
            cur.execute(query_insert, ['test7', '20', 'テストデータを挿入します'])
            conn.commit()
        except Exception as e:
            print(e.args)
            # ロールバック
            conn.rollback()
            cur.close()
            conn.close()
            raise Exception

        cur.execute(query_select)
        rows = cur.fetchall()
        print('insert row is', rows[-1])
        self.assertEqual(rows[-1][1], 'test7')
        cur.close()
        conn.close()


if __name__ == '__main__':
    unittest.main()
