"""Domain model representing an agent within the Eagle Eye DB application."""

class Agent:
    """Agent class."""
    def __init__(self, id, code_name, real_name, location, status, missions_completed):
        """__init__ function."""
        self.__id = id
        self.code_name = code_name
        self.real_name = real_name
        self.location = location
        self.status = status
        self.missions_completed = missions_completed

    def __str__(self):
        """__str__ function."""
        return (f"\n{self.__class__.__name__} id: {self.__id}\n"
                f"Code name: {self.code_name}\n"
                f"Name: {self.real_name}\n"
                f"Location: {self.location}\n"
                f"Status: {self.status}\n"
                f"Missions completed: {self.missions_completed}")



