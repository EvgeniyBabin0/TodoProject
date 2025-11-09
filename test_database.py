import mongomock
import pytest

import database


@pytest.fixture
def mock_mongo(monkeypatch):
    client = mongomock.MongoClient()
    monkeypatch.setattr(database, "client", client)
    monkeypatch.setattr(database, "db", client.todo_db)
    monkeypatch.setattr(database, "tasks_collection", client.todo_db.tasks)
    yield


def test_create_task(mock_mongo):
    task_data = {"title": "Test task", "completed": False}
    new_task = database.create_task(task_data)
    assert "id" in new_task

    tasks = database.get_all_tasks()
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Test task"


def test_update_task(mock_mongo):
    task_data = {"title": "Old title", "completed": False}
    new_task = database.create_task(task_data)
    updated_data = {"title": "New title", "completed": True}
    updated = database.update_task(new_task["id"], updated_data)
    assert updated is True

    updated_task = database.get_task(new_task["id"])
    assert updated_task["title"] == "New title"
    assert updated_task["completed"] is True


def test_delete_task(mock_mongo):
    task_data = {"title": "Task to delete", "completed": False}
    new_task = database.create_task(task_data)
    deleted = database.delete_task(new_task["id"])
    assert deleted is True

    tasks = database.get_all_tasks()
    assert len(tasks) == 0
