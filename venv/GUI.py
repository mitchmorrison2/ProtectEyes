import PySimpleGUI as sg

sg.theme('Purple')	# Add a touch of color
# All the stuff inside your window.


layout = [  [sg.Text('Brightness Modifier', size=(30,1), font='Default 18'), sg.Button('On', font='Default 18'), sg.Button('Off', font='Default 18')],
            [sg.Text('Time interval between breaks (min): ',font='Default 18', size=(30,1)), sg.InputText('20', font='Default 18',size=(10,15))],
            [sg.Text('Break period (sec): ', font='Default 18', size=(30,1)), sg.InputText('20',font='Default 18', size=(10,15))],
            [sg.Button('Close', font='Default 18')]]

# Create the Window

window = sg.Window('Protect Your Eyes!', layout, default_element_size = (40, 1))
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Close'):	# if user closes window or clicks cancel
        break
    if event in (None, 'On'):
        window['On'].update(disabled=True)
        window['Off'].update(disabled=False)
    if event in (None, 'Off'):
        window['On'].update(disabled=False)
        window['Off'].update(disabled=True)
    break_time = values[0]
    dim_screen_time = values[1]
    print(values[0], values[1])

window.close()
