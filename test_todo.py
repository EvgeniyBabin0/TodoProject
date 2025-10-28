import json

import pytest

from main import Task, TodoList


def test_task_attributes_covered():
    t = Task("Test")
    assert hasattr(t, "title")
    assert hasattr(t, "completed")
    assert hasattr(t, "created_at")

def test_complete_task_out_of_bounds():
    todo = TodoList()
    todo.add_task("Task 1")
    assert not todo.complete_task(-5)
    assert not todo.complete_task(100)

def test_remove_task_out_of_bounds():
    todo = TodoList()
    todo.add_task("Task 1")
    assert not todo.remove_task(-1)
    assert not todo.remove_task(50)

def test_save_tasks_creates_file(tmp_path):
    todo = TodoList()
    todo.add_task("Task A")
    file_path = tmp_path / "tasks.json"
    todo.save_tasks(str(file_path))
    assert file_path.exists()
    content = file_path.read_text(encoding='utf-8')
    assert "Task A" in content

def test_load_tasks_correct_json(tmp_path):
    data = [
        {"title": "task1", "completed": False},
        {"title": "task2", "completed": True}
    ]
    file_path = tmp_path / "tasks.json"
    file_path.write_text(json.dumps(data), encoding='utf-8')

    todo = TodoList()
    todo.load_tasks(str(file_path))

    assert len(todo.get_all()) == 2
    assert todo.get_all()[0].title == "task1"
    assert todo.get_all()[1].completed is True

def test_load_tasks_file_not_found():
    todo = TodoList()
    todo.load_tasks("nonexistent_file.json")
    assert todo.get_all() == []

def test_load_tasks_invalid_json(tmp_path):
    file_path = tmp_path / "bad.json"
    file_path.write_text("not a json", encoding='utf-8')

    todo = TodoList()
    with pytest.raises(json.JSONDecodeError):
        todo.load_tasks(str(file_path))

def test_load_tasks_zip_strict_false(tmp_path):
    data = [
        {"title": "task1", "completed": False},
    ]
    file_path = tmp_path / "tasks.json"
    file_path.write_text(json.dumps(data), encoding='utf-8')

    todo = TodoList()
    todo.load_tasks(str(file_path))
    assert len(todo.get_all()) == 1

def test_main_entry_point(monkeypatch):
    import main
    monkeypatch.setattr(main.TodoList, "save_tasks", lambda self, filename: None)
    main.main()
