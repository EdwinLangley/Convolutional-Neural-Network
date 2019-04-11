import unittest
from databasehelper import database_object
from unittest.mock import MagicMock,Mock
import sqlite3



class TestClass(unittest.TestCase):

    def test_sqlite_connection(self):
        sqlite3.connect = MagicMock(return_value='connection succeeded')

        databaseclass = database_object()
        sqlite3.connect.assert_called_with('db/predictions.db')
        self.assertEqual(databaseclass.create_connection(),'connection succeeded')


if __name__ == '__main__':
    unittest.main()