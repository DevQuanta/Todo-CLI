class Tasks:
    def __init__(self):
        self.tasks = []
        self._index = 0

    def __repr__(self):
        return f"{self.tasks}"

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self.tasks):
            task = self.tasks[self._index]
            self._index += 1
            return task
        else:
            raise StopIteration

    def __getitem__(self, item):
        return self.tasks[item]

    def __len__(self):
        return len(self.tasks)
