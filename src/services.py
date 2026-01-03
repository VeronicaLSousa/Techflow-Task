# Regras de negócio do sistema

from models import Task

class TaskService:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        self.tasks.append(Task(title))
