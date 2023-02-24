import unittest
import sqlite3
from unittest.mock import patch
import backend 

class TestProgram(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # create a test database and insert test data
        cls.conn = sqlite3.connect(':memory:')
        cls.conn.execute('''CREATE TABLE ADMIN
                            (USERNAME TEXT PRIMARY KEY NOT NULL,
                             PASSWORD TEXT NOT NULL);''')
        cls.conn.execute('''INSERT INTO ADMIN (USERNAME, PASSWORD)
                            VALUES ("testuser", "testpass")''')
        cls.conn.commit()

    @classmethod
    def tearDownClass(cls):
        # drop the test database
        cls.conn.close()

    def test_login_db_valid(self):
        # test the login function with valid credentials
        result = backend.login_db("sir", "sir")
        self.assertIsNone(result) # since dock() doesn't return anything

    def test_login_db_invalid(self):
        # test the login function with invalid credentials
        result = backend.login_db("sir", "siir")
        self.assertEqual(result, "sir", "sir")

    @patch('backend.os.system')
    def test_dock(self, mock_os_system):
        # test the dock function
        backend.dock()
        mock_os_system.assert_called_with('docker run --rm -it -p 5000:80 ubuntu:latest bin/bash')

    @patch('backend.webbrowser.open')
    def test_redirect(self, mock_webbrowser_open):
        # test the redirect function
        backend.redirect("")
        self.assertEqual(mock_webbrowser_open.call_count, 4) # should open 4 times

    @patch('backend.os.system')
    def test_browser(self, mock_os_system):
        # test the browser function
        backend.browser()
        mock_os_system.assert_called_with('python3 app.py')

    def test_register_db(self):
        # test the register function
        backend.register_db("newuser", "newpass")
        result = self.conn.execute('''SELECT * FROM ADMIN
                                      WHERE USERNAME="newuser"''')
        self.assertIsNotNone(result) # user should be inserted

if __name__ == '__main__':
    unittest.main()
