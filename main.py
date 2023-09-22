import PySimpleGUI as sg
import os
from zipfile import ZipFile

label1 = sg.Text("Select files to compress:")
label2 = sg.Text("Select destination folder:")
inp_box1 = sg.InputText(tooltip="Enter todo",key="compress",size=30)
inp_box2 = sg.InputText(tooltip="Enter todo",key="destination",size=30)
button_chose1 = sg.FilesBrowse("Choose")
button_chose2 = sg.FolderBrowse("Choose")
button_compress = sg.Button("Compress",key="button_compress")
layout= [[label1,inp_box1,button_chose1],[label2,inp_box2,button_chose2],[button_compress]]
window = sg.Window("My To-Do App",
                   layout=layout,
                   font=("Helvetica",20))

def compress_button(zipname):
    with ZipFile(zipname,"w") as zipobject:
        zipobject.write(values["compress"])

is_going_on = True
while is_going_on:
    event,values = window.read()
    print(1, event)
    print(2, values)
    print(3, values["compress"])
    print(4, values["destination"])

    match event:
        case "button_compress":
            zip_name = values["compress"].split("/")
            zip_name = zip_name[-1]+".zip"
            compress_button(values["destination"]+"/"+zip_name)
            if os.path.exists(values["destination"]+"/"+zip_name):
                print(zip_name)
                print("ZIP file created")
            else:
                print("ZIP file not created")

        case sg.WIN_CLOSED:
            break

print("Good Bye!")