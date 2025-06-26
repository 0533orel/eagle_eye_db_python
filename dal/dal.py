from db_connection import SQLConnection
from models.agent import Agent

connection = SQLConnection("eagleeyedb")

class DALAgent:
    def add(self):
        try:
            conn = connection.open_connection()
            cursor = conn.cursor()
            query = ("INSERT INTO agents (code_name, real_name, location) VALUES (%s, %s, %s)")
            full_name = input("Enter full name: ")
            code_name = input("Enter code name: ")
            location = input("Enter location: ")
            value = (code_name, full_name, location)
            cursor.execute(query, value)
            conn.commit()
            print("Agent added successfully")
        except Exception as ex:
            print(ex)
        finally:
            connection.close_connection(conn)

