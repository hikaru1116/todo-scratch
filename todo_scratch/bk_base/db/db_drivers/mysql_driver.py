
from typing import Dict, Tuple
from todo_scratch.bk_base.db.db_drivers.db_driver import DbDriver
import mysql.connector as mysql
from todo_scratch.bk_base.util.settings_util import get_member_by_settings
from mysql.connector import (connection)


class MySqlDriver(DbDriver):
    DB_CONFIG_SETTING_NAME = "DB_CONFIG"

    connector: connection.MySQLConnection = None

    def __enter__(self,):
        self.connect()

    def __exit__(self, exc_type, exc_value, traceback):
        self.disconnect()

    def connect(self, is_transaction=False):
        db_config = get_member_by_settings(self.DB_CONFIG_SETTING_NAME)

        if not db_config:
            raise Exception('not exist db config')

        self.connector = mysql.connect(**db_config)
        self.connector.autocommit = not is_transaction

    def disconnect(self,):
        self.connector.close()

    def commit(self,):
        self.connector.commit()

    def rollback(self):
        self.connector.rollback()

    def is_connect(self,) -> bool:
        if not self.connector:
            return False
        return self.connector.is_connected()

    def query(self, query: str) -> Dict:
        cur = self.connector.cursor(dictionary=True)

        cur.execute(query)
        rows = cur.fetchall()
        return rows

    def query_with_param(self, query: str, param: Tuple) -> Dict:

        cur = self.connector.cursor(dictionary=True)

        cur.execute(query, param)
        rows = cur.fetchall()
        return rows
