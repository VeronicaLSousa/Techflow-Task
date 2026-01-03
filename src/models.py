# Modelos de dados do sistema

class Task:
    def __init__(self, id, title, status="A Fazer"):
        self.id = id
        self.title = title
        self.status = status

    def __repr__(self):
        return f"[{self.id}] {self.title} - {self.status}"

