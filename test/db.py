import pymysql.cursors
import unittest
import sys
# importモジュールのディレクトリを設定
sys.path.append('../')


class TestTemplate(unittest.TestCase):
    """DB関連の処理テスト

    Args:
        unittest (_type_): ユニットテスト
    """

    def test_class_loader(self):
        connection = pymysql.connect(host='192.168.64.3',
                                     user='admin',
                                     password='P@ssw0rd',
                                     database='todo_scratch',
                                     cursorclass=pymysql.cursors.DictCursor)
        with connection:
            # with connection.cursor() as cursor:
            #     # Create a new record
            #     sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
            #     cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

            # # connection is not autocommit by default. So you must commit to save
            # # your changes.
            # connection.commit()

            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT * FROM `user` WHERE `id`=%s"
                cursor.execute(sql, (1,))
                result = cursor.fetchone()
                print(result)

        self.assertEqual('hikaru', result.get('name'))


if __name__ == '__main__':
    unittest.main()
