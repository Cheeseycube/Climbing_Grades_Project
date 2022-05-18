# Climbing Grade Project
# Data Exploration

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE


mydata = pd.read_excel("Climbing_Stats.xlsx")


mydata = mydata.drop('Observations', 1) # Dropping the observations column. 1 for cols, 0 for rows
mydata = mydata.drop('Size of holds', 1)
mydata = mydata.drop('Distance between holds for intended beta', 1)

    
tempdata = mydata


# dropping empty rows at the bottom
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


