import json


class LocalStorage:
    def __init__(self, fp):
        self.fp = fp

    def commit(self, tasks):
        with open(self.fp, "w") as file:
            json.dump([task.__dict__ for task in tasks], file, indent=4)

    def fetch(self):
        with open(self.fp, "r") as file:
            tasks = json.load(file)

        return tasks
