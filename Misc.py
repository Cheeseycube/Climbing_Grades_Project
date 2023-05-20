import pandas as pd
import Climbing_Grade_Proj_Functions as Functions
import matplotlib.pyplot as plt
import seaborn as sns
from openpyxl import load_workbook



if __name__ == "__main__":
    workbook = load_workbook(filename="Climbing_Stats_ProjectVersion.xlsx")
    sheet1 = workbook['Sheet1']

    '''df = pd.read_excel("Climbing_Stats_ProjectVersion.xlsx", "Sheet2")
    df = df.drop(df.columns[0], axis=1)
    df = df.reset_index()

    for index, row in df.iterrows():
        new_row = (row['Given Grade'], row['Wall angle'], row['Overall distance (ft)'], row['Number of footholds'],
                   row['Easy crimps'], row['medium crimps'], row['difficult crimps'], row['extreme crimps'],
                   row['Jugs'], row['Shallow Jugs'], row['Slopers'], row['Underclings'], row['Total Crimps'],
                   row['Jugs'] + row['Shallow Jugs'], row['Num. handholds'], row['Number of footholds'])
        sheet1.append(new_row)

    workbook.save("Climbing_Stats_ProjectVersion.xlsx")'''

