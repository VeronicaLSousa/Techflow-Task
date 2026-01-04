# Arquivo principal da aplicação

# app.py
# Camada de controle (API REST)

from flask import Flask, jsonify, request
from src import services

app = Flask(__name__)


@app.route("/tasks", methods=["GET"])
def list_tasks():
    status_filter = request.args.get("status")  # Novo parâmetro
    tasks_list = services.get_all_tasks(status=status_filter)
    return jsonify(tasks_list), 200

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()

    if not data or "title" not in data or "priority" not in data:
        return jsonify({"error": "Dados inválidos"}), 400

    task = services.create_task(
        title=data["title"],
        priority=data["priority"]
    )

    return jsonify(task), 201


@app.route("/tasks/<int:task_id>", methods=["PUT", "PATCH"])
def update_task(task_id):
    data = request.get_json()

    if not data:
        return jsonify({"error": "Dados inválidos"}), 400

    task = services.update_task(
        task_id,
        title=data.get("title"),
        priority=data.get("priority"),
        status=data.get("status")
    )

    if not task:
        return jsonify({"error": "Tarefa não encontrada"}), 404

    return jsonify(task), 200


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    success = services.delete_task(task_id)

    if not success:
        return jsonify({"error": "Tarefa não encontrada"}), 404

    return jsonify({"message": "Tarefa removida com sucesso"}), 200


if __name__ == "__main__":
    app.run(debug=True)
