import PySimpleGUI as sq
import functions
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sq.theme("DarkPurple")

clock = sq.Text("", key="clock")
label = sq.Text("Type in a to-do")
input_box = sq.InputText(tooltip="Enter todo", key="todo",size=46)
add_button = sq.Button("Add", size=10, key="Add")
list_box = sq.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[45, 10])
edit_button = sq.Button("Edit", size=10)
complete_button = sq.Button("Complete", size=10)
exit_button = sq.Button("Exit")
col1 =[[input_box],[list_box]]
col2 = [[add_button],[edit_button],[complete_button]]

window = sq.Window("My To-Do App",
                   layout=[[clock],
                           [label],
                           [sq.Column(col1),sq.Column(col2)],
                           [exit_button]],
                   font=("Helvetica", 15))
while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"]

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sq.popup("Please select an item first", font=("Helvetica", 20))
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sq.popup("Please select an item first", font=("Helvetica", 20))
        case "Exit":
            break
        case sq.WINDOW_CLOSED:
            break
window.close()
