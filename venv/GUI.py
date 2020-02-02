import PySimpleGUI as sg

sg.theme('DarkAmber')	# Add a touch of color
# All the stuff inside your window.


layout = [  [sg.Text('Brightness Modifier', size=(30,1)), sg.Button('On'), sg.Button('Off')],
            [sg.Text('Time interval between breaks (min): ', size=(30,1)), sg.InputText('20', size=(10,15))],
            [sg.Text('Break period (sec): ', size=(30,1)), sg.InputText('20', size=(10,15))],
            [sg.Button('Ok'), sg.Button('Close')]]

# Create the Window

window = sg.Window('Protect Your Eyes!', layout, default_element_size = (40, 1))
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Close'):	# if user closes window or clicks cancel
        break
    break_time = values[0]
    dim_screen_time = values[1]
    print(values[0], values[1])
#    print('You entered ', values[0])

window.close()
