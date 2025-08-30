from fastapi import BackgroundTasks


class BackgroundQueue:
    def __init__(self):
        self.tasks = []

    def add_task(self, task, *args, **kwargs):
        self.tasks.append((task, args, kwargs))

    def process_tasks(self, background_tasks: BackgroundTasks):
        for task, args, kwargs in self.tasks:
            background_tasks.add_task(task, *args, **kwargs)
        self.tasks.clear()


background_queue = BackgroundQueue()
