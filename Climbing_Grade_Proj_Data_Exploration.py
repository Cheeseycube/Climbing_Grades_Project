# Climbing Grade Project
# Data Exploration
# test comment

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE
import seaborn as sns

mydata = pd.read_excel("Climbing_Stats_ProjectVersion.xlsx")


mydata = mydata.drop('Observations', 1) # Dropping the observations column. 1 for cols, 0 for rows
mydata = mydata.drop('Size of holds', 1)
mydata = mydata.drop('Distance between holds for intended beta', 1)

    
UnencodedData = mydata

# dropping empty rows at the bottom   This works by checking each index in the original dataset, then removing that specific row from the new dataset regardless of index
# first argument is row to start on, second is one over the row to end on
for x in range(21, 29):
    UnencodedData = UnencodedData.drop([mydata.index[x]])
    
#UnencodedData = UnencodedData.drop([mydata.index[17], mydata.index[18]])

mydata = UnencodedData

# this is the same dataset but without any dummy-encoding
UnencodedData = UnencodedData.fillna(0)


mis_val = mydata.isnull().sum()
mydata = mydata.fillna(0)
mydata = pd.get_dummies(mydata, columns =["Given Grade"], prefix = ["V"])



# practicing data visualization techniques...

# FOR DUMMY ENCODED VARIABLES
# prints out the number of jugs for each V0

print("Number of jugs for each V0:")
for i in mydata.index:
    #print(mydata["V_0.0"][i], mydata["V_1.0"][i])
    if (mydata["V_0.0"][i] == 1):
        print(mydata["Jugs"][i])
        
print()
print("Same thing but using different code:")

# FOR NON-DUMMY ENCODED VARS
for i in UnencodedData.index:
    if(UnencodedData["Given Grade"][i] == 0):
        print(UnencodedData["Jugs"][i])
        




# JUG DISTRIBUTION CHARTS

# distribution including entire dataset
#sns.displot(UnencodedData, x="Jugs")

# creating a dataset with only V0s
V0data = UnencodedData
for i in UnencodedData.index:
    if (UnencodedData["Given Grade"][i] != 0):
        V0data = V0data.drop([UnencodedData.index[i]])

# distribution of jugs for V0s only        
sns.displot(V0data, x="Jugs").set(title = 'Jug Distribution for V0')


# creating a dataset with only V1s
V1data = UnencodedData
for i in UnencodedData.index:
    if (UnencodedData["Given Grade"][i] != 1):
        V1data = V1data.drop([UnencodedData.index[i]])

# distribution of jugs for V1s only        
sns.displot(V1data, x="Jugs").set(title = 'Jug Distribution for V1')


# creating a dataset with only V2s
V2data = UnencodedData
for i in UnencodedData.index:
    if (UnencodedData["Given Grade"][i] != 2):
        V2data = V2data.drop([UnencodedData.index[i]])

# distribution of jugs for V2s only        
sns.displot(V2data, x="Jugs").set(title = 'Jug Distribution for V2')

# creating a dataset with only V3s
V3data = UnencodedData
for i in UnencodedData.index:
    if (UnencodedData["Given Grade"][i] != 3):
        V3data = V3data.drop([UnencodedData.index[i]])

# distribution of jugs for V3s only        
sns.displot(V3data, x="Jugs").set(title = 'Jug Distribution for V3')

# creating a dataset with only V4s
V4data = UnencodedData
for i in UnencodedData.index:
    if (UnencodedData["Given Grade"][i] != 4):
        V4data = V4data.drop([UnencodedData.index[i]])

# distribution of jugs for V4s only        
sns.displot(V4data, x="Jugs").set(title = 'Jug Distribution for V4')



# idea: look at num footholds / total length or num handholds / total length

# research maximum liklihood estimation

# NUMBER OF FOOTHOLDS DISTRIBUTION CHART

# creating a dataset with only V0s
V0data = UnencodedData
for i in UnencodedData.index:
    if (UnencodedData["Given Grade"][i] != 0):
        V0data = V0data.drop([UnencodedData.index[i]])

# distribution of Number of footholds for V0s only        
sns.displot(V0data, x="Number of footholds").set(title = 'Foothold distribution for V0')


# creating a dataset with only V1s
V1data = UnencodedData
for i in UnencodedData.index:
    if (UnencodedData["Given Grade"][i] != 1):
        V1data = V1data.drop([UnencodedData.index[i]])

# distribution of Number of footholds for V1s only        
sns.displot(V1data, x="Number of footholds").set(title = 'Foothold distribution for V1')


# creating a dataset with only V2s
V2data = UnencodedData
for i in UnencodedData.index:
    if (UnencodedData["Given Grade"][i] != 2):
        V2data = V2data.drop([UnencodedData.index[i]])

# distribution of Number of footholds for V2s only        
sns.displot(V2data, x="Number of footholds").set(title = 'Foothold distribution for V2')

# creating a dataset with only V3s
V3data = UnencodedData
for i in UnencodedData.index:
    if (UnencodedData["Given Grade"][i] != 3):
        V3data = V3data.drop([UnencodedData.index[i]])

# distribution of Number of footholds for V3s only        
sns.displot(V3data, x="Number of footholds").set(title = 'Foothold distribution for V3')



#  TOTAL CRIMPS DISTRIBUTION CHART

# creating a dataset with only V0s
V0data = UnencodedData
for i in UnencodedData.index:
    if (UnencodedData["Given Grade"][i] != 0):
        V0data = V0data.drop([UnencodedData.index[i]])

# distribution of Total Crimps for V0s only        
sns.displot(V0data, x="Total Crimps")


# creating a dataset with only V1s
V1data = UnencodedData
for i in UnencodedData.index:
    if (UnencodedData["Given Grade"][i] != 1):
        V1data = V1data.drop([UnencodedData.index[i]])

# distribution of Total Crimps for V1s only        
sns.displot(V1data, x="Total Crimps")


# creating a dataset with only V2s
V2data = UnencodedData
for i in UnencodedData.index:
    if (UnencodedData["Given Grade"][i] != 2):
        V2data = V2data.drop([UnencodedData.index[i]])

# distribution of Total Crimps for V2s only        
sns.displot(V2data, x="Total Crimps")

# creating a dataset with only V3s
V3data = UnencodedData
for i in UnencodedData.index:
    if (UnencodedData["Given Grade"][i] != 3):
        V3data = V3data.drop([UnencodedData.index[i]])

# distribution of Total Crimps for V3s only        
sns.displot(V3data, x="Total Crimps")




# DIFFICULT CRIMPS DISTRIBUTION CHARTS

# creating a dataset with only V0s
V0data = UnencodedData
for i in UnencodedData.index:
    if (UnencodedData["Given Grade"][i] != 0):
        V0data = V0data.drop([UnencodedData.index[i]])

# distribution of difficult Crimps for V0s only        
sns.displot(V0data, x="difficult crimps").set(title = "Difficult Crimps Distribution for V0")


# creating a dataset with only V1s
V1data = UnencodedData
for i in UnencodedData.index:
    if (UnencodedData["Given Grade"][i] != 1):
        V1data = V1data.drop([UnencodedData.index[i]])

# distribution of difficult Crimps for V1s only        
sns.displot(V1data, x="difficult crimps").set(title = "Difficult Crimps Distribution for V1")


# creating a dataset with only V2s
V2data = UnencodedData
for i in UnencodedData.index:
    if (UnencodedData["Given Grade"][i] != 2):
        V2data = V2data.drop([UnencodedData.index[i]])

# distribution of difficult Crimps for V2s only        
sns.displot(V2data, x="difficult crimps").set(title = "Difficult Crimps Distribution Chart for V2")

# creating a dataset with only V3s
V3data = UnencodedData
for i in UnencodedData.index:
    if (UnencodedData["Given Grade"][i] != 3):
        V3data = V3data.drop([UnencodedData.index[i]])

# distribution of difficult Crimps for V3s only        
sns.displot(V3data, x="difficult crimps").set(title = "Difficult Crimps Distribution Chart for V3")