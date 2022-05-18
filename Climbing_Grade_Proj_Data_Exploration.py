# Climbing Grade Project
# Data Exploration

import pandas as pd
import numpy as np
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


mis_val = mydata.isnull().sum()
mydata = mydata.fillna(0)
#mydata = pd.get_dummies(mydata, columns =["Given Grade"], prefix = ["V"])






