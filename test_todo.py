import os
import json
import pytest
from datetime import datetime
from main import TodoList, Task

def test_task_init():
    t = Task("Test task")
    assert t.title == "Test task"
    assert t.completed is False
    assert isinstance(t.created_at, datetime)

def test_task_init_attributes():
    t = Task("Example task")
    assert t.title == "Example task"
    assert t.completed is False
    assert hasattr(t, "created_at")

def test_complete_task_return_value():
    todo = TodoList()
    todo.add_task("Task")
    assert todo.complete_task(0) is True
    assert todo.get_all()[0].completed is True
    assert todo.complete_task(1) is False
def test_complete_task_invalid_index():
    todo = TodoList()
    todo.add_task("Task")
    assert todo.complete_task(10) is False
    assert todo.complete_task(-1) is False

def test_complete_task_invalid_indices():
    todo = TodoList()
    todo.add_task("Sample")
    assert todo.complete_task(-1) is False
    assert todo.complete_task(100) is False

def test_remove_task():
    todo = TodoList()
    todo.add_task("Задача 1")
    todo.add_task("Задача 2")
    assert len(todo.get_all()) == 2

    assert todo.remove_task(0) is True
    assert len(todo.get_all()) == 1
    assert todo.get_all()[0].title == "Задача 2"

    assert todo.remove_task(10) is False
    assert len(todo.get_all()) == 1

def test_save_and_load_tasks(tmp_path):
    todo = TodoList()
    todo.add_task("Первая задача")
    todo.add_task("Вторая задача")
    todo.complete_task(1)

    file_path = tmp_path / "tasks.json"
    todo.save_tasks(str(file_path))

    assert file_path.exists()
    with open(file_path, encoding='utf-8') as f:
        data = f.read()
    assert "Первая задача" in data
    assert "Вторая задача" in data

    new_todo = TodoList()
    new_todo.load_tasks(str(file_path))

    assert len(new_todo.get_all()) == 2
    assert new_todo.get_all()[0].title == "Первая задача"
    assert new_todo.get_all()[1].completed is True

def test_load_tasks_nonexistent_file():
    todo = TodoList()
    todo.load_tasks("nonexistent_file.json")
    assert todo.get_all() == []

def test_save_load_empty_file(tmp_path):
    file_path = tmp_path / "empty.json"
    file_path.write_text("[]", encoding='utf-8')

    todo = TodoList()
    todo.load_tasks(str(file_path))
    assert todo.get_all() == []

def test_load_tasks_invalid_json(tmp_path):
    file_path = tmp_path / "invalid.json"
    file_path.write_text("invalid json content", encoding="utf-8")

    todo = TodoList()
    with pytest.raises(json.JSONDecodeError):
        todo.load_tasks(str(file_path))
