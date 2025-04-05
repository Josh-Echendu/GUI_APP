import functions
import PySimpleGUI as sg

label = sg.Text("Type in a To-Do")#this is used to create a label on the window
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

window = sg.Window('My To-Do App',
                    layout=[[label],[input_box, add_button]]) #this is used to crete a window
window.read() #this create the wimdows on the screen
window.close()