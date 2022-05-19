# Climbing Grade Project
# Data Exploration

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE
import seaborn as sns

mydata = pd.read_excel("Climbing_Stats.xlsx")


mydata = mydata.drop('Observations', 1) # Dropping the observations column. 1 for cols, 0 for rows
mydata = mydata.drop('Size of holds', 1)
mydata = mydata.drop('Distance between holds for intended beta', 1)

    
tempdata = mydata


# dropping empty rows at the bottom   This works by checking each index in the original dataset, then removing that specific row from the new dataset regardless of index
for x in range(19, 29):
    tempdata = tempdata.drop([mydata.index[x]])
    
#tempdata = tempdata.drop([mydata.index[17], mydata.index[18]])

mydata = tempdata

# this is the same dataset but without any dummy-encoding
tempdata = tempdata.fillna(0)


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
for i in tempdata.index:
    if(tempdata["Given Grade"][i] == 0):
        print(tempdata["Jugs"][i])
        

# need to make a distribution chart for grades and number of jugs

# distribution including entire dataset
sns.displot(tempdata, x="Jugs")

# creating a dataset with only V0s
V0data = tempdata
for i in tempdata.index:
    if (tempdata["Given Grade"][i] != 0):
        V0data = V0data.drop([tempdata.index[i]])

# distribution of jugs for V0s only        
sns.displot(V0data, x="Jugs")


# creating a dataset with only V1s
V1data = tempdata
for i in tempdata.index:
    if (tempdata["Given Grade"][i] != 1):
        V1data = V1data.drop([tempdata.index[i]])

# distribution of jugs for V1s only        
sns.displot(V1data, x="Jugs")


# creating a dataset with only V2s
V2data = tempdata
for i in tempdata.index:
    if (tempdata["Given Grade"][i] != 2):
        V2data = V2data.drop([tempdata.index[i]])

# distribution of jugs for V2s only        
sns.displot(V2data, x="Jugs")

# creating a dataset with only V3s
V3data = tempdata
for i in tempdata.index:
    if (tempdata["Given Grade"][i] != 3):
        V3data = V3data.drop([tempdata.index[i]])

# distribution of jugs for V3s only        
sns.displot(V3data, x="Jugs")

