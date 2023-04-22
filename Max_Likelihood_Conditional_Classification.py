# Climbing Grade Project 
# Max Likliehood Conditional Classification
# This is similar to maximumum liklihood classification but it enables the use of more variables

# check independence with chi-squared test of independence, the null is independent
# do this by making the two way table and putting that in a chi-squared calculator

import pandas as pd
import numpy as np
import sys
from matplotlib import pyplot as plt
import Climbing_Grade_Proj_Functions as Functions

# GETTING THE DATA
df = Functions.get_data()

# Binning Jugs
min_value = df['Jugs'].min()
max_value = df['Jugs'].max()
JugBins = np.linspace(min_value, max_value, 4)
labels = ['small', 'medium', 'big']
df['Jugs_binned'] = pd.cut(df['Jugs'], bins = JugBins, labels = labels, include_lowest = True)
df["Jugs_binned"].value_counts().sort_index().plot(kind = "bar", title = "Binned Jugs Distribution")
plt.show()


# Binning Footholds
min_value = df['Number of footholds'].min()
max_value = df['Number of footholds'].max()
FootholdBins = np.linspace(min_value, max_value, 4)
labels = ['small', 'medium', 'big']
df['Footholds_binned'] = pd.cut(df['Number of footholds'], bins = FootholdBins, labels = labels, include_lowest = True)
df["Footholds_binned"].value_counts().sort_index().plot(kind = "bar", title = "Binned Footholds Distribution")
plt.show()


# Binning total crimps
min_value = df['Total Crimps'].min()
max_value = df['Total Crimps'].max()
TotalCrimpsBins = np.linspace(min_value, max_value, 4)
labels = ['small', 'medium', 'big']
df['Total_Crimps_Binned'] = pd.cut(df['Total Crimps'], bins = TotalCrimpsBins, labels = labels, include_lowest = True)
df["Total_Crimps_Binned"].value_counts().sort_index().plot(kind = "bar", title = "Binned Total Crimps Distribution")
plt.show()

# Binning extreme crimps
min_value = df['extreme crimps'].min()
max_value = df['extreme crimps'].max()
ExtremeCrimpsBins = np.linspace(min_value, max_value, 3)
labels = ['small', 'big']
df['Extreme_Crimps_Binned'] = pd.cut(df['extreme crimps'], bins = ExtremeCrimpsBins, labels = labels, include_lowest = True)
df["Extreme_Crimps_Binned"].value_counts().sort_index().plot(kind = "bar", title = "Binned Extreme Crimps Distribution")
plt.show()


''' USER INTERFACE BEGIN'''
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
V0data = Functions.createV0Data(df)
V0_count = len(V0data.index)

V1data = Functions.createV1Data(df)
V1_count = len(V1data.index)

V2data = Functions.createV2Data(df)
V2_count = len(V2data.index)

V3data = Functions.createV3Data(df)
V3_count = len(V3data.index)

V4data = Functions.createV4Data(df)
V4_count = len(V4data.index)

V7data = Functions.createV7Data(df)
V7_count = len(V7data.index)

V10data = Functions.createV10Data(df)
V10_count = len(V10data.index)

# PROBABILITY OF THE DATA OCCURRING GIVEN EACH GRADE
ProbData_GivenV0 = ((V0data["Jugs_binned"].value_counts()[jugInput] / V0_count)
                    * (V0data["Footholds_binned"].value_counts()[footInput] / V0_count)
                    * (V0data["Total_Crimps_Binned"].value_counts()[crimpInput]/ V0_count)
                    * (V0data["Extreme_Crimps_Binned"].value_counts()[extremecrimpInput]/ V0_count))

ProbData_GivenV1 = ((V1data["Jugs_binned"].value_counts()[jugInput] / V1_count)
                    * (V1data["Footholds_binned"].value_counts()[footInput] / V1_count)
                    * (V1data["Total_Crimps_Binned"].value_counts()[crimpInput]/ V1_count)
                    * (V1data["Extreme_Crimps_Binned"].value_counts()[extremecrimpInput]/ V1_count))

ProbData_GivenV2 = ((V2data["Jugs_binned"].value_counts()[jugInput] / V2_count)
                    * (V2data["Footholds_binned"].value_counts()[footInput] / V2_count)
                    * (V2data["Total_Crimps_Binned"].value_counts()[crimpInput]/ V2_count)
                    * (V2data["Extreme_Crimps_Binned"].value_counts()[extremecrimpInput]/ V2_count))

ProbData_GivenV3 = ((V3data["Jugs_binned"].value_counts()[jugInput] / V3_count)
                    * (V3data["Footholds_binned"].value_counts()[footInput] / V3_count)
                    * (V3data["Total_Crimps_Binned"].value_counts()[crimpInput]/ V3_count)
                    * (V3data["Extreme_Crimps_Binned"].value_counts()[extremecrimpInput]/ V3_count))

ProbData_GivenV4 = ((V4data["Jugs_binned"].value_counts()[jugInput] / V4_count)
                    * (V4data["Footholds_binned"].value_counts()[footInput] / V4_count)
                    * (V4data["Total_Crimps_Binned"].value_counts()[crimpInput]/ V4_count)
                    * (V4data["Extreme_Crimps_Binned"].value_counts()[extremecrimpInput]/ V4_count))

ProbData_GivenV7 = ((V7data["Jugs_binned"].value_counts()[jugInput] / V7_count)
                    * (V7data["Footholds_binned"].value_counts()[footInput] / V7_count)
                    * (V7data["Total_Crimps_Binned"].value_counts()[crimpInput]/ V7_count)
                    * (V7data["Extreme_Crimps_Binned"].value_counts()[extremecrimpInput]/ V7_count))

ProbData_GivenV10 = ((V10data["Jugs_binned"].value_counts()[jugInput] / V10_count)
                    * (V10data["Footholds_binned"].value_counts()[footInput] / V10_count)
                    * (V10data["Total_Crimps_Binned"].value_counts()[crimpInput]/ V10_count)
                    * (V10data["Extreme_Crimps_Binned"].value_counts()[extremecrimpInput]/ V10_count))

# PROBABILITY OF EACH GRADE OCCURRING IN GENERAL
total_row_count = len(df.index)
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
























