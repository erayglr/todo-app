import PySimpleGUI as sq
import functions
import time

sq.theme("DarkPurple")

clock = sq.Text("", key="clock")
label = sq.Text("Type in a to-do")
input_box = sq.InputText(tooltip="Enter todo", key="todo")
add_button = sq.Button(size=2, image_source="add.png", mouseover_colors="LightBlue2", tooltip="Add Todo", key="Add")
list_box = sq.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[45, 10])
edit_button = sq.Button("Edit")
complete_button = sq.Button(size=5, image_source="complete.png", mouseover_colors="LightBlue2", tooltip="Complete Todo"
                                                                                                        ,key="Complete")
exit_button = sq.Button("Exit")

window = sq.Window("My To-Do App",
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
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
