import functions
import PySimpleGUI as sg

label = sg.Text("Type in a To-Do")#this is used to create a label on the window
input_box = sg.InputText(tooltip="Enter todo", key = "todo")
add_button = sg.Button("Add")

window = sg.Window('My To-Do App',
        layout=[[label],[input_box, add_button]],
        font=("Helvetica", 20)) #this is used to crete a window

while True:
    event, values = window.read() #the read method returns something that why we put it a variable
    print('event = ', event)
    print('values = ', values)
    
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"]
            todos.append(new_todo)
            functions.write_todos(todos)
        
        case sg.WIN_CLOSED:
            break 
window.close()

#commit message "we implemented an ADD button"

































































