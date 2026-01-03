# Arquivo principal da aplicação

from flask import Flask, jsonify, request
from services import TaskService

app = Flask(__name__)
service = TaskService()

@app.route("/")
def home():
    return {"message": "TechFlow Task Manager API"}

@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = service.list_tasks()
    return jsonify([task.__dict__ for task in tasks])

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    title = data.get("title")
    task = service.create_task(title)
    return jsonify(task.__dict__), 201

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json()
    status = data.get("status")
    task = service.update_task(task_id, status)
    if task:
        return jsonify(task.__dict__)
    return {"error": "Tarefa não encontrada"}, 404

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    if service.delete_task(task_id):
        return {"message": "Tarefa removida"}
    return {"error": "Tarefa não encontrada"}, 404

if __name__ == "__main__":
    app.run(debug=True)


