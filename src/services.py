# Regras de negócio do sistema

from models import Task


class TaskService:
    """
    Classe responsável pela regra de negócio do gerenciamento de tarefas.
    Implementa as operações CRUD (Create, Read, Update, Delete).
    """

    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def create_task(self, title):
        """
        Cria uma nova tarefa.
        :param title: título da tarefa
        :return: objeto Task ou None se título inválido
        """
        if not title or not isinstance(title, str):
            return None

        task = Task(
            id=self.next_id,
            title=title.strip(),
            status="A Fazer"
        )

        self.tasks.append(task)
        self.next_id += 1
        return task

    def list_tasks(self):
        """
        Retorna a lista de tarefas cadastradas.
        """
        return self.tasks

    def get_task_by_id(self, task_id):
        """
        Busca uma tarefa pelo ID.
        :param task_id: ID da tarefa
        :return: Task ou None
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id, status):
        """
        Atualiza o status de uma tarefa existente.
        :param task_id: ID da tarefa
        :param status: novo status
        :return: Task atualizada ou None se não encontrada
        """
        task = self.get_task_by_id(task_id)

        if not task or not status:
            return None

        task.status = status.strip()
        return task

    def delete_task(self, task_id):
        """
        Remove uma tarefa pelo ID.
        :param task_id: ID da tarefa
        :return: True se removida, False caso contrário
        """
        task = self.get_task_by_id(task_id)

        if not task:
            return False

        self.tasks.remove(task)
        return True
