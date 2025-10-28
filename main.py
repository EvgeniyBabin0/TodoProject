from datetime import datetime

class Task:
    def __init__(self, title: str):
        self.title = title
        self.completed = False
        self.created_at = datetime.now()

    def mark_completed(self):
        self.completed = True


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title: str):
        self.tasks.append(Task(title))

    def complete_task(self, index: int):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()

    def get_all(self):
        return self.tasks

    def get_incomplete(self):
        return [t for t in self.tasks if not t.completed]



if __name__ == "__main__":
    todo_list = TodoList()
    todo_list.add_task("Написать отчёт")
    todo_list.add_task("Купить продукты")
    todo_list.add_task("Позвонить врачу")
    todo_list.add_task("Сделать домашнее задание")
    todo_list.add_task("Прочитать главу учебника")
    todo_list.add_task("Сходить в спортзал")
    todo_list.add_task("Подготовить презентацию")
    todo_list.add_task("Забрать посылку с почты")
    todo_list.add_task("Оплатить квитанции")
    todo_list.add_task("Поздравить друга с днём рождения")

    # Отмечаем как выполненные несколько задач
    todo_list.complete_task(1)  # "Купить продукты"
    todo_list.complete_task(4)  # "Прочитать главу учебника"
    todo_list.complete_task(7)  # "Забрать посылку с почты"

    print("Все задачи:")
    for t in todo_list.get_all():
        print(f"- {t.title}: {'✓' if t.completed else '✗'}")

    print("\nНевыполненные задачи:")
    for t in todo_list.get_incomplete():
        print(f"- {t.title}")