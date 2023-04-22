
import pandas as pd
import Climbing_Grade_Proj_Functions as Functions
import PySimpleGUI as sg
import sys

if __name__ == "__main__":
    df = Functions.get_data()

    layout = [
                [sg.Text("Given Grade", font=("Helvetica", 20), size=(15, 1)), sg.InputText(size=(5, 10), font=("Helvetica", 20))],
                [sg.Text("Overall Distance (ft)", font=("Helvetica", 20), size=(15, 1)), sg.InputText(size=(5, 10), font=("Helvetica", 20))],
                [sg.Text("Wall Angle", font=("Helvetica", 20), size=(15, 1)), sg.InputText(size=(5, 10), font=("Helvetica", 20))],
                [sg.Text("Footholds", font=("Helvetica", 20), size=(15, 1)), sg.InputText(size=(5, 10), font=("Helvetica", 20))],
                [sg.Text("Jugs", font=("Helvetica", 20), size=(15, 1)), sg.InputText(size=(5, 10), font=("Helvetica", 20))],
                [sg.Text("Shallow Jugs", font=("Helvetica", 20), size=(15, 1)), sg.InputText(size=(5, 10), font=("Helvetica", 20))],
                [sg.Text("Easy Crimps", font=("Helvetica", 20), size=(15, 1)), sg.InputText(size=(5, 10), font=("Helvetica", 20))],
                [sg.Text("Medium Crimps", font=("Helvetica", 20), size=(15, 1)), sg.InputText(size=(5, 10), font=("Helvetica", 20))],
                [sg.Text("Difficult Crimps", font=("Helvetica", 20), size=(15, 1)), sg.InputText(size=(5, 10), font=("Helvetica", 20))],
                [sg.Text("Extreme Crimps", font=("Helvetica", 20), size=(15, 1)), sg.InputText(size=(5, 10), font=("Helvetica", 20))],
                [sg.Text("Underclings", font=("Helvetica", 20), size=(15, 1)), sg.InputText(size=(5, 10), font=("Helvetica", 20))],
                [sg.Text("Slopers", font=("Helvetica", 20), size=(15, 1)), sg.InputText(size=(5, 10), font=("Helvetica", 20))],
                [sg.Submit(size=(10, 5), font=("Helvetica", 20))]
             ]

    MainWindow = sg.Window('Add to database program', layout, margins=(50, 50), element_justification='c')

    while True:
        event, values = MainWindow.read()
        if (event == sg.WIN_CLOSED or event == 'Exit'):
            MainWindow.close()
            break
        if (event == 'Submit'):
            print("submitted")
            MainWindow.close()
            break

    for i in range(12):
        if values[i] == '':
            values[i] = 0
    try:
        grade = int(values[0])
        distance = float(values[1])
        angle = int(values[2])
        footholds = int(values[3])
        jugs = int(values[4])
        shallow_jugs = int(values[5])
        easy_crimps = int(values[6])
        medium_crimps = int(values[7])
        difficult_crimps = int(values[8])
        extreme_crimps = int(values[9])
        underclings = int(values[10])
        slopers = int(values[11])
    except:
        sg.popup('Invalid data, cancelled add')
        sys.exit(0)


    newRow = {
                'Given Grade': [grade],
                'Overall distance (ft)': [distance],
                'Wall angle': [angle],
                'Number of footholds': [footholds],
                'Jugs': [jugs],
                'Shallow Jugs': [shallow_jugs],
                'Easy crimps': [easy_crimps],
                'medium crimps': [medium_crimps],
                'difficult crimps': [difficult_crimps],
                'extreme crimps': [extreme_crimps],
                'Underclings': [underclings],
                'Slopers': [slopers]
             }

    new_df = pd.DataFrame(newRow)

    try:
        df = pd.concat([df, new_df])
        df.to_excel("Climbing_Stats_ProjectVersion.xlsx")
        sg.popup('Successfully added the following new row:', newRow)
    except:
        sg.popup('Encountered an error when adding the new row:', newRow)





