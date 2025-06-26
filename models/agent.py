class Agent:
    def __init__(self, id, code_name, real_name, location, status, missions_completed):
        self._id = id
        self.code_name = code_name
        self.real_name = real_name
        self.location = location
        self.status = status
        self.missions_completed = missions_completed

    def __str__(self):
        return (f"\n{self.__class__.__name__}\n"
                f"Code name {self.code_name}\n"
                f"Name: {self.real_name}\n"
                f"Location: {self.location}\n"
                f"Status: {self.status}\n"
                f"Missions completed: {self.missions_completed}")



