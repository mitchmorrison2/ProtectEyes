import PySimpleGUI as sg

sg.theme('DarkAmber')	# Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Brightness Modifier'), sg.Button('On'), sg.Button('Off')],
            [sg.Text('Time interval between breaks: '), sg.InputText(), sg.Button('Ok')],
            [sg.Button('Close')]]

# Create the Window
window = sg.Window('Protect Your Eyes!', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Close'):	# if user closes window or clicks cancel
        break
    timeBtwnDim = values[0]
    print(values[0])
#    print('You entered ', values[0])

window.close()
