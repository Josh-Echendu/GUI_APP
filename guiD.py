import functions
import PySimpleGUI as sg

label = sg.Text("Type in a To-Do")#this is used to create a label on the window
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

list_box = sg.Listbox(values=functions.get_todos(),
                    key="todos", enable_events=True, size=[45, 10])#values of a list box expects a list

edit_button = sg.Button("Edit")

window = sg.Window('My To-Do App',
        layout=[[label],[input_box, add_button], [list_box, edit_button]],
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
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"]
            new_todo = todo_to_edit
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            
            todos[index] = new_todo
            
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        
        case "todos":
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break 
window.close()

# commit messaga "implement of the Edit button"

































































