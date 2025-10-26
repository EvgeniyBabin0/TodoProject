from main import TodoList

def test_add_task():
    todo = TodoList()
    todo.add_task("Купить хлеб")
    assert len(todo.get_all()) == 1

def test_complete_task():
    todo = TodoList()
    todo.add_task("Позвонить врачу")
    todo.complete_task(0)
    assert todo.get_all()[0].completed is True

def test_incomplete():
    todo = TodoList()
    todo.add_task("Почистить зубы")
    assert len(todo.get_incomplete()) == 1