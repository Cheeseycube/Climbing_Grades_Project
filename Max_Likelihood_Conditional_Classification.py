# Climbing Grade Project 
# Max Likliehood Conditional Classification

# check independence with chi-squared test of independence, the null is independent
# do this by making the two way table and putting that in a chi-squared calculator

import pandas as pd
import numpy as np
import sys
from matplotlib import pyplot as plt

# IMPORTING AND CLEANING THE DATA
mydata = pd.read_excel("Climbing_Stats_ProjectVersion.xlsx")


mydata = mydata.drop('Observations', 1) # Dropping the observations column. 1 for cols, 0 for rows
mydata = mydata.drop('Size of holds', 1)
mydata = mydata.drop('Distance between holds for intended beta', 1)

tempdata = mydata

for x in range(25, 29):
    tempdata = tempdata.drop([mydata.index[x]])
    

tempdata = tempdata.fillna(0)    
mis_val = tempdata.isnull().sum()
mydata = tempdata

#V0Test = mydata.iloc[0]
#V0Test = mydata.iloc[5]

#V1Test = mydata.iloc[1]
#V1Test = mydata.iloc[2]

#V2Test = mydata.iloc[3]
#V2Test = mydata.iloc[4]

#V3Test = mydata.iloc[6]
#V3Test = mydata.iloc[10]

#V4Test = mydata.iloc[21]

#mydata = mydata.drop([6])
#mydata = mydata.reset_index()

# Binning Jugs
min_value = mydata['Jugs'].min()
max_value = mydata['Jugs'].max()

JugBins = np.linspace(min_value, max_value, 4)
labels = ['small', 'medium', 'big']
mydata['Jugs_binned'] = pd.cut(mydata['Jugs'], bins = JugBins, labels = labels, include_lowest = True)

mydata["Jugs_binned"].value_counts().sort_index().plot(kind = "bar", title = "Binned Jugs Distribution")
plt.show()


# Binning Footholds
min_value = mydata['Number of footholds'].min()
max_value = mydata['Number of footholds'].max()

FootholdBins = np.linspace(min_value, max_value, 4)
labels = ['small', 'medium', 'big']
mydata['Footholds_binned'] = pd.cut(mydata['Number of footholds'], bins = FootholdBins, labels = labels, include_lowest = True)

mydata["Footholds_binned"].value_counts().sort_index().plot(kind = "bar", title = "Binned Footholds Distribution")
plt.show()


# Binning total crimps
min_value = mydata['Total Crimps'].min()
max_value = mydata['Total Crimps'].max()

TotalCrimpsBins = np.linspace(min_value, max_value, 4)
labels = ['small', 'medium', 'big']
mydata['Total_Crimps_Binned'] = pd.cut(mydata['Total Crimps'], bins = TotalCrimpsBins, labels = labels, include_lowest = True)

mydata["Total_Crimps_Binned"].value_counts().sort_index().plot(kind = "bar", title = "Binned Total Crimps Distribution")
plt.show()

# Binning extreme crimps
min_value = mydata['extreme crimps'].min()
max_value = mydata['extreme crimps'].max()

ExtremeCrimpsBins = np.linspace(min_value, max_value, 3)
labels = ['small', 'big']
mydata['Extreme_Crimps_Binned'] = pd.cut(mydata['extreme crimps'], bins = ExtremeCrimpsBins, labels = labels, include_lowest = True)

mydata["Extreme_Crimps_Binned"].value_counts().sort_index().plot(kind = "bar", title = "Binned Extreme Crimps Distribution")
plt.show()


''' USER INTERFACE BEGIN'''
#print(V3Test)
print()
print("Welcome to my experimental Climbing Grade Program!")
print("If you provide the following measurements for a climb this program will attempt to predict the grade:")
print("Number of Jugs, Number of Footholds, Number of Crimps (any size), Number of Extreme Crimps")

numJugs = int(input("Please provide the number of jugs here:\n"))
jugInput = ""
if numJugs in range(0, 6):
    print(f"{numJugs} is a small amount of jugs")
    jugInput = "small"

elif numJugs in range(6, 11):
    print(f"{numJugs} is a medium amount of jugs")
    jugInput = "medium"

else:
    print(f"{numJugs} is a large amount of jugs")
    jugInput = "big"


numFootholds = int(input("Please provide the number of footholds here:\n"))
footInput = ""
if numFootholds in range(0, 8):
    print(f"{numFootholds} is a small amount of footholds")
    footInput = "small"

elif numFootholds in range(8, 15):
    print(f"{numFootholds} is a medium amount of footholds")
    footInput = "medium"

else:
    print(f"{numFootholds} is a large amount of footholds")
    footInput = "big"

numCrimps = int(input("Please provide the number of crimps here:\n"))
crimpInput = ""
if numCrimps in range(0, 4):
    print(f"{numCrimps} is a small amount of crimps")
    crimpInput = "small"

elif numCrimps in range(4, 8):
    print(f"{numCrimps} is a medium amount of crimps")
    crimpInput = "medium"

else:
    print(f"{numCrimps} is a large amount of crimps")
    crimpInput = "big"
    
numExtremeCrimps = int(input("Please provide the number of extreme crimps here:\n"))
extremecrimpInput = ""
if numExtremeCrimps in range(0, 1):   # change this threshold if I don't want every extreme crimp to be automatic v10
    print(f"{numExtremeCrimps} is a small amount of extreme crimps")
    extremecrimpInput = "small"

else:
    print(f"{numExtremeCrimps} is a large amount of extreme crimps")
    extremecrimpInput = "big"
    
''' USER INTERFACE END'''


# Creating necessary dataframes
V0data = mydata
for i in mydata.index:
    if (mydata["Given Grade"][i] != 0):
        V0data = V0data.drop([mydata.index[i]])
        
V1data = mydata
for i in mydata.index:
    if (mydata["Given Grade"][i] != 1):
        V1data = V1data.drop([mydata.index[i]])

V2data = mydata
for i in mydata.index:
    if (mydata["Given Grade"][i] != 2):
        V2data = V2data.drop([mydata.index[i]])

V3data = mydata
for i in mydata.index:
    if (mydata["Given Grade"][i] != 3):
        V3data = V3data.drop([mydata.index[i]])
        
V4data = mydata
for i in mydata.index:
    if (mydata["Given Grade"][i] != 4):
        V4data = V4data.drop([mydata.index[i]])
        
V7data = mydata
for i in mydata.index:
    if (mydata["Given Grade"][i] != 7):
        V7data = V7data.drop([mydata.index[i]])

V10data = mydata
for i in mydata.index:
    if (mydata["Given Grade"][i] != 10):
        V10data = V10data.drop([mydata.index[i]])
        
        
        

# PROBABILITY OF THE DATA OCCURRING GIVEN EACH GRADE
ProbData_GivenV0 = ((V0data["Jugs_binned"].value_counts()[jugInput] / len(V0data.index))
                    * (V0data["Footholds_binned"].value_counts()[footInput] / len(V0data.index)) 
                    * (V0data["Total_Crimps_Binned"].value_counts()[crimpInput]/ len(V0data.index))
                    * (V0data["Extreme_Crimps_Binned"].value_counts()[extremecrimpInput]/ len(V0data.index)))

ProbData_GivenV1 = ((V1data["Jugs_binned"].value_counts()[jugInput] / len(V1data.index)) 
                    * (V1data["Footholds_binned"].value_counts()[footInput] / len(V1data.index)) 
                    * (V1data["Total_Crimps_Binned"].value_counts()[crimpInput]/ len(V1data.index))
                    * (V1data["Extreme_Crimps_Binned"].value_counts()[extremecrimpInput]/ len(V1data.index)))

ProbData_GivenV2 = ((V2data["Jugs_binned"].value_counts()[jugInput] / len(V2data.index)) 
                    * (V2data["Footholds_binned"].value_counts()[footInput] / len(V2data.index)) 
                    * (V2data["Total_Crimps_Binned"].value_counts()[crimpInput]/ len(V2data.index))
                    * (V2data["Extreme_Crimps_Binned"].value_counts()[extremecrimpInput]/ len(V2data.index)))

ProbData_GivenV3 = ((V3data["Jugs_binned"].value_counts()[jugInput] / len(V3data.index)) 
                    * (V3data["Footholds_binned"].value_counts()[footInput] / len(V3data.index)) 
                    * (V3data["Total_Crimps_Binned"].value_counts()[crimpInput]/ len(V3data.index))
                    * (V3data["Extreme_Crimps_Binned"].value_counts()[extremecrimpInput]/ len(V3data.index)))

ProbData_GivenV4 = ((V4data["Jugs_binned"].value_counts()[jugInput] / len(V4data.index)) 
                    * (V4data["Footholds_binned"].value_counts()[footInput] / len(V4data.index)) 
                    * (V4data["Total_Crimps_Binned"].value_counts()[crimpInput]/ len(V4data.index))
                    * (V4data["Extreme_Crimps_Binned"].value_counts()[extremecrimpInput]/ len(V4data.index)))

ProbData_GivenV7 = ((V7data["Jugs_binned"].value_counts()[jugInput] / len(V7data.index)) 
                    * (V7data["Footholds_binned"].value_counts()[footInput] / len(V7data.index)) 
                    * (V7data["Total_Crimps_Binned"].value_counts()[crimpInput]/ len(V7data.index))
                    * (V7data["Extreme_Crimps_Binned"].value_counts()[extremecrimpInput]/ len(V7data.index)))

ProbData_GivenV10 = ((V10data["Jugs_binned"].value_counts()[jugInput] / len(V10data.index)) 
                    * (V10data["Footholds_binned"].value_counts()[footInput] / len(V10data.index)) 
                    * (V10data["Total_Crimps_Binned"].value_counts()[crimpInput]/ len(V10data.index))
                    * (V10data["Extreme_Crimps_Binned"].value_counts()[extremecrimpInput]/ len(V10data.index)))

# PROBABILITY OF EACH GRADE OCCURRING IN GENERAL
total_row_count = len(mydata.index)
Prob_V0 = V0data["Jugs_binned"].size / total_row_count
Prob_V1 = V1data["Jugs_binned"].size / total_row_count
Prob_V2 = V2data["Jugs_binned"].size / total_row_count
Prob_V3 = V3data["Jugs_binned"].size / total_row_count
Prob_V4 = V4data["Jugs_binned"].size / total_row_count
Prob_V7 = V7data["Jugs_binned"].size / total_row_count
Prob_V10 = V10data["Jugs_binned"].size / total_row_count




GivenData_Divided_By_Alldata = ((ProbData_GivenV0 * len(V0data.index)) + (ProbData_GivenV1 * len(V1data.index)) 
                                + (ProbData_GivenV2 * len(V2data.index)) + (ProbData_GivenV3 * len(V3data.index)) 
                                + (ProbData_GivenV4 * len(V4data.index)) + (ProbData_GivenV7 * len(V7data.index))
                                + (ProbData_GivenV10 * len(V10data.index))) / total_row_count 

#error catching
if GivenData_Divided_By_Alldata == 0:
    print("Insufficient data to estimate this climb's grade, quitting program")
    sys.exit(0)

ProbV0_GivenData = ProbData_GivenV0 * Prob_V0 / GivenData_Divided_By_Alldata
ProbV1_GivenData = ProbData_GivenV1 * Prob_V1 / GivenData_Divided_By_Alldata
ProbV2_GivenData = ProbData_GivenV2 * Prob_V2 / GivenData_Divided_By_Alldata
ProbV3_GivenData = ProbData_GivenV3 * Prob_V3 / GivenData_Divided_By_Alldata
ProbV4_GivenData = ProbData_GivenV4 * Prob_V4 / GivenData_Divided_By_Alldata
ProbV7_GivenData = ProbData_GivenV7 * Prob_V7 / GivenData_Divided_By_Alldata
ProbV10_GivenData = ProbData_GivenV10 * Prob_V10 / GivenData_Divided_By_Alldata


''' USER INTERFACE '''

print("The program gives the following probabilities for each grade:\n")
print(f"V0: {ProbV0_GivenData * 100:.2f}%")
print(f"V1: {ProbV1_GivenData * 100:.2f}%")
print(f"V2: {ProbV2_GivenData * 100:.2f}%")
print(f"V3: {ProbV3_GivenData * 100:.2f}%")
print(f"V4: {ProbV4_GivenData * 100:.2f}%")
print(f"V7: {ProbV7_GivenData * 100:.2f}%")
print(f"V10: {ProbV10_GivenData * 100:.2f}%")
























