import PySimpleGUI as sg
import os

sg.theme('Purple')	# Add a touch of color
# All the stuff inside your window.
file = "preferences.txt"
break_time = 20
dim_screen_time = 20

if os.stat(file).st_size != 0:
    opened = open(file, "r")
    break_time, dim_screen_time = map(int, opened.readline().split())

layout = [  [sg.Text('Brightness Modifier', size=(30,1), font='Default 18'), sg.Button('On', font='Default 18'), sg.Button('Off', font='Default 18')],
            [sg.Text('Time interval between breaks (min): ',font='Default 18', size=(30,1)), sg.InputText(break_time, font='Default 18',size=(10,15))],
            [sg.Text('Break period (sec): ', font='Default 18', size=(30,1)), sg.InputText(dim_screen_time, font='Default 18', size=(10,15))],
            [sg.Button('Close', font='Default 18')]]

# Create the Window

window = sg.Window('Protect Your Eyes!', layout, default_element_size = (40, 1))
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'On'):
        window['On'].update(disabled=True)
        window['Off'].update(disabled=False)
        #Le code for on goes here
    if event in (None, 'Off'):
        window['On'].update(disabled=False)
        window['Off'].update(disabled=True)
        #Code for off goes here
    break_time = values[0]
    dim_screen_time = values[1]
    f = open(file, "w")
    f.write(break_time + ' ' + dim_screen_time)
    #print(values[0], values[1])
    if event in (None, 'Close'):	# if user closes window or clicks cancel
        break

window.close()
