import mysql.connector
from mysql.connector import errors

class SQLConnection:
    def __init__(self, db_name):
        self.conn_str = {
            "host": "localhost",
            "user": "root",
            "password": "",
            "database": db_name
        }

    def open_connection(self):
        try:
            connection = mysql.connector.connect(**self.conn_str)
            return connection
        except errors as e:
            print(f"Error while connecting to MySQL: {e}")
            return None

    def close_connection(self, connection):
        if connection.is_connected:
            connection.close()
