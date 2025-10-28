import json
from datetime import datetime


class Task:
    def __init__(self, title: str):
        self.title = title
        self.completed = False
        self.created_at = datetime.now()

    def mark_completed(self):
        self.completed = True

    def __repr__(self):
        status = "✓" if self.completed else "✗"
        return f"Task(title={self.title!r}, completed={status})"


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title: str):
        self.tasks.append(Task(title))

    def complete_task(self, index: int) -> bool:
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
            return True
        return False

    def remove_task(self, index: int) -> bool:
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            return True
        return False

    def get_all(self):
        return self.tasks

    def get_incomplete(self):
        return [t for t in self.tasks if not t.completed]

    def save_tasks(self, filename: str):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(
                [{'title': t.title, 'completed': t.completed} for t in self.tasks],
                f,
                ensure_ascii=False,
                indent=2
            )

    def load_tasks(self, filename: str):
        try:
            with open(filename, encoding='utf-8') as f:
                data = json.load(f)
                self.tasks = [Task(item['title']) for item in data]
                for t, item in zip(self.tasks, data, strict=True):
                    t.completed = item['completed']
        except FileNotFoundError:
            self.tasks = []  # Обнуляем список, если файла нет


def main():
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

    todo_list.complete_task(1)
    todo_list.complete_task(4)
    todo_list.complete_task(7)

    print("Все задачи:")
    for t in todo_list.get_all():
        print(f"- {t.title}: {'✓' if t.completed else '✗'}")

    print("\nНевыполненные задачи:")
    for t in todo_list.get_incomplete():
        print(f"- {t.title}")

    todo_list.save_tasks("tasks.json")


if __name__ == "__main__":
    main()
