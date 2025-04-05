import PySimpleGUI as sg
import zip_creator

label = sg.Text('Select file to compress: ')
choose_button = sg.FilesBrowse("choose", key= "files") #FilesBrowse is a specil button used to select files, and we want to select more than one zip file
input_button = sg.InputText(tooltip='Enter a file')


label2 = sg.Text('Select destination folder: ')
choose_button2 = sg.FolderBrowse("choose", key= "folder")# FolderBrowse is a special button used to select folders
input_button2 = sg.InputText(tooltip='Enter a file')

compress_button = sg.Button("compress")
output_label = sg.Text(key="output", text_color = "gold")


window = sg.Window('File compressor',
                layout=[[label, input_button, choose_button],
                        [label2, input_button2, choose_button2],
                        [compress_button, output_label]])

while True:
        event, values = window.read()
        print(event)
        print(values)

        filepath = values["files"].split(";")
        folderpath = values["folder"]
        zip_creator.make_archive(filepath, folderpath)
        window["output"].update(value="Compression complete!!!!")

        match event:
                case sg.WIN_CLOSED:
                        break
window.close()   