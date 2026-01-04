# Testes automatizados do sistema de tarefas

import json
import pytest
from src.app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_create_task(client):
    response = client.post(
        "/tasks",
        data=json.dumps({
            "title": "Tarefa de teste",
            "priority": "Alta"
        }),
        content_type="application/json"
    )

    assert response.status_code == 201
    data = response.get_json()
    assert data["title"] == "Tarefa de teste"
    assert data["priority"] == "Alta"
    assert data["status"] == "A Fazer"


def test_get_tasks(client):
    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)


def test_update_task_status(client):
    response = client.patch(
        "/tasks/1",
        data=json.dumps({"status": "Concluído"}),
        content_type="application/json"
    )

    assert response.status_code == 200
    assert response.get_json()["status"] == "Concluído"


def test_update_task_title(client):
    response = client.patch(
        "/tasks/1",
        data=json.dumps({"title": "Novo título"}),
        content_type="application/json"
    )

    assert response.status_code == 200
    assert response.get_json()["title"] == "Novo título"


def test_delete_task(client):
    response = client.delete("/tasks/1")
    assert response.status_code == 200

def test_get_tasks_filtered_by_status(client):
    # Cria duas tarefas com status diferente
    client.post("/tasks", json={"title": "Tarefa 1", "priority": "Alta"})
    client.post("/tasks", json={"title": "Tarefa 2", "priority": "Média"})
    
    # Atualiza a primeira tarefa para Concluído
    client.patch("/tasks/1", json={"status": "Concluído"})
    
    # Filtra por status Concluído
    response = client.get("/tasks?status=Concluído")
    data = response.get_json()
    
    assert response.status_code == 200
    assert len(data) == 1
    assert data[0]["status"] == "Concluído"

