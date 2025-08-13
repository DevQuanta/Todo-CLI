from Todo_CLI.models.task import Task
from Todo_CLI.models.tasks import Tasks


class TaskService:
    def __init__(self, storage=None):
        self.storage = storage
        self.tasks = self.fetch()

    def fetch(self):
        self.tasks = Tasks()

        tasks = self.storage.fetch()

        for task in tasks:
            task_name = task["name"]
            task_status = task["status"]
            task_notes = task["notes"]

            self.add_task(task_name, task_status, task_notes)

        return self.tasks

    def commit(self):
        self.storage.commit(self.tasks)

    def add_task(self, name, status, notes):
        new_task = Task(name, status, notes)
        self.tasks.tasks.append(new_task)

    def change_task(self, idx, name, status, notes):
        if name:
            self.tasks[idx].name = name
        if status:
            self.tasks[idx].status = status
        if notes:
            self.tasks[idx].notes = notes

    def remove_task(self, idx):
        self.tasks.tasks.pop(idx)

    def list_tasks(self):
        return self.tasks
