import functions
import PySimpleGUI as sg
import time

sg.theme("DarkPurple4")
clock_label = sg.Text("The time is", key='clock')
label = sg.Text("Type in a To-Do")#this is used to create a label on the window
input_box = sg.InputText(tooltip="Enter todo", key="todo")


list_box = sg.Listbox(values=functions.get_todos(),
                    key="todos", enable_events=True, size=[45, 10])#values of a list box expects a list

add_button = sg.Button("Add", size=10)
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window('My To-Do App',
        layout=[[clock_label], [label], [input_box, add_button], [list_box, edit_button, complete_button], [exit_button]],
        font=("Helvetica", 20)) #this is used to crete a window

while True:
    event, values = window.read(timeout=200) #the read method returns something that why we put it a variable
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo) 
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:    
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"]
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                
                todos[index] = new_todo
                
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item please.", font=("Helvetica", 20))    
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                index = todos.index(todo_to_complete)
                todos.pop(index)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item.")

        case "todos":
            window['todo'].update(value=values['todos'][0])

        case "Exit":
            break      
        case sg.WIN_CLOSED:
            break 
window.close()

# we changed time, added clock, handled edit and complete error
