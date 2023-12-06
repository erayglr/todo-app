import PySimpleGUI as sq
import functions

label = sq.Text("Type in a to-do")
input_box = sq.InputText(tooltip="Enter todo")
add_button = sq.Button("Add")
window = sq.Window("My To-Do App", layout=[[label], [input_box, add_button]])
window.read()
window.close()
