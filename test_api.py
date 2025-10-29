import requests

BASE_URL = "http://localhost:8008"

def test_create_task():
    data = {"title": "Тестовая задача"}
    response = requests.post(f"{BASE_URL}/tasks", json=data)
    assert response.status_code in (200, 201)
    task = response.json()
    assert "id" in task
    assert task["title"] == data["title"]

def test_delete_task():
    response = requests.delete(f"{BASE_URL}/tasks/1")
    assert response.status_code == 200

def test_get_tasks():
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_update_task():
    data = {"title": "Обновленная задача", "completed": True}
    response = requests.put(f"{BASE_URL}/tasks/1", json=data)
    assert response.status_code == 200
    task = response.json()
    assert task["title"] == data["title"]
    assert task["completed"] is True
