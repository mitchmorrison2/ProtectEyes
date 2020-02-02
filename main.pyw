import PySimpleGUI as sg
import os, time, wmi, platform

current_brightness = wmi.WMI(namespace='wmi').WmiMonitorBrightness()[0].CurrentBrightness
user_system = platform.system()

if (user_system != 'Windows'):
    sg.popup('This app only works in Windows')
    exit(0)

def turn_off_screen(secs):
    wmi.WMI(namespace='wmi').WmiMonitorBrightnessMethods()[0].WmiSetBrightness(0, 0)
    time.sleep(secs)

def turn_on_screen():
    wmi.WMI(namespace='wmi').WmiMonitorBrightnessMethods()[0].WmiSetBrightness(current_brightness, 0)

# Add a touch of color
sg.theme('Purple')  

# All the stuff inside your window.
file = "preferences.txt"
break_time = 20
dim_screen_time = 20

if os.stat(file).st_size != 0:
    opened = open(file, "r")
    break_time, dim_screen_time = map(int, opened.readline().split())

layout = [  [sg.Text('Brightness Modifier', size=(30,1), font='Default 18'), sg.Button('On', font='Default 18'), sg.Button('Off', font='Default 18', disabled=True)],
            [sg.Text('Time interval between breaks (min): ',font='Default 18', size=(30,1)), sg.InputText(break_time, key='break_time', font='Default 18',size=(10,15))],
            [sg.Text('Break period (sec): ', font='Default 18', size=(30,1)), sg.InputText(dim_screen_time, key='dim_screen_time', font='Default 18', size=(10,15))],
            [sg.Button('Save and Close', font='Default 18')]]

# Create the Window
window = sg.Window('Protect Your Eyes!', layout, default_element_size = (40, 1))

# Event Loop to process "events" and get the "values" of the inputs
time_passed = 0
is_running = False

while True:
    event, values = window.read(timeout=1000)
    time_passed += 1

    print(time_passed, is_running)

    break_time = values['break_time']
    dim_screen_time = values['dim_screen_time']
    
    if (event == 'On'):
        try:
            break_time = int(break_time)
            dim_screen_time = int(dim_screen_time)
            if (break_time < 0) or (dim_screen_time < 0):
                raise Exception('Negative numbers')
            window['On'].update(disabled=True)
            window['Off'].update(disabled=False)
            window['break_time'].update(disabled=True)
            window['dim_screen_time'].update(disabled=True)
            is_running = True
        except:
            sg.popup('Make sure your inputs are positive integers!')
            
    if event == 'Off':
        window['On'].update(disabled=False)
        window['Off'].update(disabled=True)
        window['break_time'].update(disabled=False)
        window['dim_screen_time'].update(disabled=False)
        is_running = False

    if (is_running == True):
        if (time_passed >= int(break_time) * 60):
            turn_off_screen(int(dim_screen_time))
            turn_on_screen()
            time_passed = 0

    if (is_running == False):
        time_passed = 0

    if event == 'Save and Close':    # if user closes window or clicks cancel
        print(break_time, dim_screen_time, file=open('preferences.txt', 'w'))
        break

window.close()