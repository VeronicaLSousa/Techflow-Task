# Regras de negócio do sistema

from models import Task


tasks = []
current_id = 1


def get_all_tasks(status=None):
    if status:
        return [task for task in tasks if task["status"] == status]
    return tasks


def create_task(title, priority):
    """Cria uma nova tarefa"""
    global current_id

    task = {
        "id": current_id,
        "title": title,
        "priority": priority,
        "status": "A Fazer"
    }

    tasks.append(task)
    current_id += 1
    return task


def get_task_by_id(task_id):
    """Busca uma tarefa pelo ID"""
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None


def update_task(task_id, title=None, priority=None, status=None):
    """Atualiza uma tarefa existente"""
    task = get_task_by_id(task_id)

    if not task:
        return None

    if title:
        task["title"] = title
    if priority:
        task["priority"] = priority
    if status:
        task["status"] = status

    return task


def delete_task(task_id):
    """Remove uma tarefa"""
    global tasks
    task = get_task_by_id(task_id)

    if not task:
        return False

    tasks = [t for t in tasks if t["id"] != task_id]
    return True