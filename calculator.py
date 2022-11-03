import PySimpleGUI as sg

sg.theme('DarkBlue14')
layout = [
    [sg.Text('x: '), sg.Input(key='_X_'), sg.Text('y: '), sg.Input(key = '_Y_')],
    [sg.Button('+'), sg.Button('-'), sg.Button('*'), sg.Button('/')]
]

window = sg.Window('Calculator', layout=layout)

while True:
    event, values = window.read()

    if event == None:
        break
    try:
        x = float(values['_X_'])
        y = float(values['_Y_'])
    except ValueError:
        sg.popup('One of the values is not a number.')
    else: 
        if event == '+':
            sg.popup(f'{x} + {y} = {x+y}')
        if event == '-':
            sg.popup(f'{x} - {y} = {x-y}')
        if event == '*':
            sg.popup(f'{x} * {y} = {x*y}')
        if event == '/':
            try:
                sg.popup(f'{x} / {y} = {x/y}')
            except ZeroDivisionError:
                sg.popup('Zero Division is not allowed.')

window.close()
