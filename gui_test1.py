import functions_feet
import PySimpleGUI as sg

sg.theme("Black")
label = sg.Text("Enter feet: ")
input_box = sg.InputText(tooltip="Enter feet", key="feet")

label2 = sg.Text("Enter inches: ")
input_box2 = sg.InputText(tooltip= "Enter inches", key="inches")

convert_button = sg.Button("Convert")
exit_button = sg.Button("Exit")
output_label = sg.Text(key= "output", text_color= "gold")

window = sg.Window("Converter", layout=[[label, input_box], [label2, input_box2], [convert_button, exit_button, output_label]])

while True:
    event, values = window.read()
    print(event)
    print(values)

    match event:
        case "Convert":
            foot = values["feet"]
            inche = values["inches"]
            todo = functions_feet.converter(foot, inche)
            window["output"].update(value= todo)

        case "Exit":
            break

        case sg.WIN_CLOSED:
            break
window.close()