import PySimpleGUI as sg

sg.theme('DarkBlue14')
layout = [
    [sg.Text('x: '), sg.Input(key='_X_', size = (6,1)), 
    sg.Text('y: '), sg.Input(key = '_Y_', size = (6,1))],
    [sg.Button('+', size = (6,1)), 
    sg.Button('-', size = (6,1)), 
    sg.Button('*', size = (6,1)), 
    sg.Button('/', size = (6,1))],
    [sg.Text('', size = (40,1), key = '_RES_')]
]

window = sg.Window('Calculator', layout=layout, 
size = (400,200), font = ('Arial', 16))

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
            window['_RES_'].Update(f'{x} + {y} = {x+y}')
        if event == '-':
            window['_RES_'].Update(f'{x} - {y} = {x-y}')
        if event == '*':
            window['_RES_'].Update(f'{x} * {y} = {x*y}')
        if event == '/':
            try:
                window['_RES_'].Update(f'{x} / {y} = {x/y}')
            except ZeroDivisionError:
                sg.popup('Zero Division is not allowed.')

window.close()
