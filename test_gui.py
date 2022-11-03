import PySimpleGUI as sg

sg.theme('DarkBlue14')

layout = [
    [sg.Text('Your name'), sg.InputText()],
    [sg.Button('Show')]
]

window = sg.Window('My first GUI application', layout = layout)


while True:
    event, values = window.read()

    if event == None:
        break

window.close()