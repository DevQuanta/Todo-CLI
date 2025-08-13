class Task:
    def __init__(self, name, status, notes):
        self.name = name
        self.status = status
        self.notes = notes

    def __repr__(self):
        return f"Task(name: '{self.name}', status: '{self.status}', notes: '{self.notes}'"

    def __del__(self):
        pass