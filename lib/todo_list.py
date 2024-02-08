from lib.todo import *

class TodoList:
    def __init__(self):
        self.todo_list = []

    def add(self, todo):
        self.todo_list.append(Todo(todo))

    def incomplete(self):
        return (todo for todo in self.todo_list if not todo.complete)

    def complete(self):
        return (todo_el for todo_el in self.todo_list if todo_el.complete)

    def give_up(self):
        for todo_el in self.todo_list:
            todo_el.mark_complete()