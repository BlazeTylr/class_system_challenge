from lib.todo import *
from lib.todo_list import *

def test_todo_class_initial_value():
    task = Todo('new task')
    actual = task.complete
    expected = False
    assert actual == expected
    
def test_todo_mark_complete():
    task = Todo('new task')
    task.mark_complete()
    actual = task.complete
    expected = True
    assert actual ==expected
    
def test_add_function_in_todolist_class():
    new_todo = TodoList()
    new_todo.add('new task')
    new_todo.add('2nd task')
    actual = new_todo.todo_list[1].task
    expected = '2nd task'
    assert actual == expected
    
def test_return_incomplete_todos():
    new_todo = TodoList()
    new_todo.add('new task')
    new_todo.add('2nd task')
    actual = [todo_el.task for todo_el in new_todo.incomplete()]
    expected = ['new task', '2nd task']
    assert actual == expected
    
def test_return_complete_todos():
    new_todo = TodoList()
    new_todo.add('new task')
    new_todo.add('2nd task')
    new_todo.give_up()
    actual = [todo_el.task for todo_el in new_todo.complete()]
    expected = ['new task', '2nd task']
    assert actual == expected