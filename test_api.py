import requests

BASE_URL = "http://localhost:8008"


def create_task_for_tests(title="Тестовая задача", completed=False):
    data = {"title": title, "completed": completed}
    response = requests.post(f"{BASE_URL}/tasks", json=data)
    assert response.status_code in (200, 201)
    return response.json()


def test_create_task():
    task = create_task_for_tests("Тестовая задача")
    assert "id" in task
    assert task["title"] == "Тестовая задача"


def test_delete_task():
    task = create_task_for_tests("Для удаления")
    task_id = task["id"]

    response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Task deleted"


def test_get_tasks():
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


def test_update_task():
    task = create_task_for_tests("Для обновления")
    task_id = task["id"]

    data = {"title": "Обновленная задача", "completed": True}
    response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=data)
    assert response.status_code == 200
    updated = response.json()
    assert updated["title"] == data["title"]
    assert updated["completed"] is True
