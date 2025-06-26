"""Data Access Layer (DAL) providing CRUD operations for agents in the Eagle Eye DB MySQL database."""

from dal.db_connection import SQLConnection
from models.agent import Agent


class DALAgent:
    """DALAgent class."""
    def __init__(self, connection):
        """__init__ function."""
        self.connection = connection

    def add(self, full_name, code_name, location):
        """add function."""
        try:
            conn = self.connection.open_connection()
            cursor = conn.cursor()
            query = "INSERT INTO agents (code_name, real_name, location) VALUES (%s, %s, %s)"
            value = (code_name, full_name, location)
            cursor.execute(query, value)
            conn.commit()
            print("\nAgent added successfully")
        except Exception as ex:
            print(ex)
        finally:
            self.connection.close_connection(conn)

    def get_agent_by_id(self, id):
        """get_agent_by_id function."""
        try:
            conn = self.connection.open_connection()
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
        except:
            print("\nThe agent not found")
            return None
        finally:
            self.connection.close_connection(conn)

    def get_agents(self):
        """get_agents function."""
        try:
            conn = self.connection.open_connection()
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
            print("\nThere are no agents")
            return []

        finally:
            self.connection.close_connection(conn)

    def update_code_name(self, id, code_name):
        """update_code_name function."""
        try:
            conn = self.connection.open_connection()
            cursor = conn.cursor()
            query = "UPDATE agents SET code_name = %s WHERE id = %s"
            value = (code_name, id)
            cursor.execute(query, value)
            conn.commit()
            print("\nCode name updated successfully.")
        except Exception as ex:
            print("Error:", ex)
        finally:
            self.connection.close_connection(conn)

    def update_name(self,id, name):
        """update_name function."""
        try:
            conn = self.connection.open_connection()
            cursor = conn.cursor()
            query = "UPDATE agents SET real_name = %s WHERE id = %s"
            value = (name, id)
            cursor.execute(query, value)
            conn.commit()
            print("\nName updated successfully.")
        except Exception as ex:
            print("Error:", ex)
        finally:
            self.connection.close_connection(conn)

    def update_location(self, id, location):
        """update_location function."""
        try:
            conn = self.connection.open_connection()
            cursor = conn.cursor()
            query = "UPDATE agents SET location = %s WHERE id = %s"
            value = (location, id)
            cursor.execute(query, value)
            conn.commit()
            print("\nLocation updated successfully.")
        except Exception as ex:
            print("Error:", ex)
        finally:
            self.connection.close_connection(conn)

    def update_status(self, id, status):
        """update_status function."""
        try:
            conn = self.connection.open_connection()
            cursor = conn.cursor()
            query = "UPDATE agents SET status = %s WHERE id = %s"
            value = (status, id)
            cursor.execute(query, value)
            conn.commit()
            print("\nStatus updated successfully.")
        except Exception as ex:
            print("Error:", ex)
        finally:
            self.connection.close_connection(conn)

    def update_missions_completed(self, id):
        """update_missions_completed function."""
        try:
            conn = self.connection.open_connection()
            cursor = conn.cursor()
            query = "UPDATE agents SET missions_completed = missions_completed + 1 WHERE id = %s"
            value = (id,)
            cursor.execute(query, value)
            conn.commit()
            print("\nMissions completed updated successfully.")
        except Exception as ex:
            print("Error:", ex)
        finally:
            self.connection.close_connection(conn)

    def delete(self, id):
        """delete function."""
        try:
            conn = self.connection.open_connection()
            cursor = conn.cursor()
            query = "DELETE FROM agents WHERE id = %s"
            cursor.execute(query, (id,))
            conn.commit()
            print("\nAgent deleted successfully.")
        except Exception as ex:
            print("Error during deletion:", ex)
        finally:
            self.connection.close_connection(conn)




