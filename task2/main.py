import PySimpleGUI as sg

orientation = [  
    [sg.Input(key='-INPUT-', expand_x=True, justification='right')],
    [sg.Button('7'), sg.Button('8'), sg.Button('9'), sg.Button('/')],
    [sg.Button('4'), sg.Button('5'), sg.Button('6'), sg.Button('*')],
    [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('-')],
    [sg.Button('0'), sg.Button('.'), sg.Button('='), sg.Button('+')],
    [sg.Button('Clear')]
]

window = sg.Window('Calculator', orientation)

expression = ''

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, 'Clear'):
        break

    if event in ['0','1','2','3','4','5','6','7','8','9']:
        expression += event
        window['-INPUT-'].update(expression)

    if event in ['/','*','-','+']:
        expression += event
        window['-INPUT-'].update(expression)

    if event == '=':
        result = eval(expression)
        window['-INPUT-'].update(result)
        expression = str(result)

window.close()