from db_connection import SQLConnection
from models.agent import Agent

connection = SQLConnection("eagleeyedb")

class DALAgent:
    def add(self, full_name, code_name, location):
        try:
            conn = connection.open_connection()
            cursor = conn.cursor()
            query = "INSERT INTO agents (code_name, real_name, location) VALUES (%s, %s, %s)"
            value = (code_name, full_name, location)
            cursor.execute(query, value)
            conn.commit()
            print("\nAgent added successfully")
        except Exception as ex:
            print(ex)
        finally:
            connection.close_connection(conn)

    def get_agent_by_id(self, id):
        try:
            conn = connection.open_connection()
            cursor = conn.cursor()
            query = "SELECT * FROM agents WHERE id = %s"
            cursor.execute(query, (id,))
            result = cursor.fetchone()
            agent = Agent(
                id=result[0],
                code_name=result[1],
                real_name=result[2],
                location=result[3],
                status=result[4],
                missions_completed=result[5]
            )
            return agent
        except Exception as ex:
            #print("Error:", ex)
            return None
        finally:
            connection.close_connection(conn)

    def get_agents(self):
        try:
            conn = connection.open_connection()
            cursor = conn.cursor()
            query = "SELECT * FROM agents"
            cursor.execute(query)
            results = cursor.fetchall()

            agents = []
            for row in results:
                agent = Agent(
                    id=row[0],
                    code_name=row[1],
                    real_name=row[2],
                    location=row[3],
                    status=row[4],
                    missions_completed=row[5]
                )
                agents.append(agent)

            return agents

        except:
            print("There are no agents")
            return []

        finally:
            connection.close_connection(conn)

    def update_code_name(self, id, code_name):
        try:
            conn = connection.open_connection()
            cursor = conn.cursor()
            query = "UPDATE agents SET code_name = %s WHERE id = %s"
            value = (code_name, id)
            cursor.execute(query, value)
            conn.commit()
            print("\nCode name updated successfully.")
        except Exception as ex:
            print("Error:", ex)
        finally:
            connection.close_connection(conn)

    def update_name(self,id, name):
        try:
            conn = connection.open_connection()
            cursor = conn.cursor()
            query = "UPDATE agents SET real_name = %s WHERE id = %s"
            value = (name, id)
            cursor.execute(query, value)
            conn.commit()
            print("\nName updated successfully.")
        except Exception as ex:
            print("Error:", ex)
        finally:
            connection.close_connection(conn)

    def update_location(self, id, location):
        try:
            conn = connection.open_connection()
            cursor = conn.cursor()
            query = "UPDATE agents SET location = %s WHERE id = %s"
            value = (location, id)
            cursor.execute(query, value)
            conn.commit()
            print("\nLocation updated successfully.")
        except Exception as ex:
            print("Error:", ex)
        finally:
            connection.close_connection(conn)

    def update_status(self, id, status):
        try:
            conn = connection.open_connection()
            cursor = conn.cursor()
            query = "UPDATE agents SET status = %s WHERE id = %s"
            value = (status, id)
            cursor.execute(query, value)
            conn.commit()
            print("\nStatus updated successfully.")
        except Exception as ex:
            print("Error:", ex)
        finally:
            connection.close_connection(conn)

    def update_missions_completed(self, id):
        try:
            conn = connection.open_connection()
            cursor = conn.cursor()
            query = "UPDATE agents SET missions_completed = missions_completed + 1 WHERE id = %s"
            value = (id,)
            cursor.execute(query, value)
            conn.commit()
            print("\nMissions completed updated successfully.")
        except Exception as ex:
            print("Error:", ex)
        finally:
            connection.close_connection(conn)


