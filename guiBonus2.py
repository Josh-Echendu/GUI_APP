import zip_extractor
import PySimpleGUI as sg

sg.theme("Black")

label1 = sg.Text("Select archive: ")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("choose", key="archive") #we want the user to select one zip file

label2 = sg.Text("Select dest dir: ")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("choose", key="folder")
extract_Button = sg.Button("Extract") 
output_label = sg.Text(key="output", text_color= "gold" )

window = sg.Window("Archive Extractor",
                    layout=[[label1, input1, choose_button1],
                            [label2, input2, choose_button2],
                            [extract_Button, output_label]])
while True:
    event, values = window.read()
    print(event)
    print(values)


    match event:
        case "Extract":
            try:
                archivepath = values["archive"]
                dest_dir_path = values["folder"]
                zip_extractor.extract_archive(archivepath, dest_dir_path)
                window["output"].update(value="Extraction completed!!!")

            except FileNotFoundError:
                sg.popup("Please choose a file, Thank you")  

        case sg.WIN_CLOSED:
            break          

window.close()