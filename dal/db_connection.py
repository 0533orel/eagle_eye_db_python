"""Utility class for opening and closing MySQL connections for Eagle Eye DB."""

import mysql.connector
from mysql.connector import errors

class SQLConnection:
    """SQLConnection class."""
    def __init__(self, db_name):
        """__init__ function."""
        self.conn_str = {
            "host": "localhost",
            "user": "root",
            "password": "",
            "database": db_name
        }

    def open_connection(self):
        """open_connection function."""
        try:
            connection = mysql.connector.connect(**self.conn_str)
            return connection
        except errors as e:
            print(f"Error while connecting to MySQL: {e}")
            return None

    def close_connection(self, connection):
        """close_connection function."""
        if connection.is_connected:
            connection.close()
