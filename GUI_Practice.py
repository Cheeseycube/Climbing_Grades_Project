# GUI Practice
# 8/10/2022

import PySimpleGUI as sg
import sys

numJugs = 0

layout = [[sg.Text("Please provide the number of jugs here")], 
          [sg.InputText()],
          [sg.Submit(), 
           sg.Cancel(),
           sg.Exit()]]

InputWindow = sg.Window('InputWindow Title', layout, margins = (100, 100))    

while True: # basically a switch statement that exits on break
    event, values = InputWindow.read()
    if (event == sg.WIN_CLOSED):
        break
    if (event == 'Exit'):
        InputWindow.close()
        print("exited")
        sys.exit(0) 
        break
    if (event == 'Submit'):
        print("submitted")
        break

# closes the window after the loop breaks
InputWindow.close()

# checking if input is an integer
try:
    numJugs = int(values[0])
except:
    numJugs = f"invalid entry: {values[0]}"
sg.popup('You entered', numJugs)



print(f"{numJugs} is what the user typed")