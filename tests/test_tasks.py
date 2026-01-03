# Testes automatizados do sistema de tarefas

import sys
import os

# Permite importar arquivos da pasta src
sys.path.append(os.path.abspath("src"))

from services import TaskService


def test_create_task():
    service = TaskService()
    task = service.create_task("Estudar GitHub")

    assert task is not None
    assert task.id == 1
    assert task.title == "Estudar GitHub"
    assert task.status == "A Fazer"


def test_list_tasks():
    service = TaskService()
    service.create_task("Tarefa 1")
    service.create_task("Tarefa 2")

    tasks = service.list_tasks()
    assert len(tasks) == 2


def test_update_task():
    service = TaskService()
    task = service.create_task("Atualizar status")

    updated_task = service.update_task(task.id, "Em Progresso")

    assert updated_task.status == "Em Progresso"


def test_delete_task():
    service = TaskService()
    task = service.create_task("Remover tarefa")

    result = service.delete_task(task.id)

    assert result is True
    assert len(service.tasks) == 0


def test_create_task_invalid_title():
    service = TaskService()
    task = service.create_task("")

    assert task is None
