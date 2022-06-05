# Climbing Grade Project
# Regression Models

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

    
tempdata = mydata


# dropping empty rows at the bottom   This works by checking each index in the original dataset, then removing that specific row from the new dataset regardless of index
# first argument is row to start on, second is one over the row to end on
for x in range(21, 29):
    tempdata = tempdata.drop([mydata.index[x]])
    
#tempdata = tempdata.drop([mydata.index[17], mydata.index[18]])

mydata = tempdata

# this is the same dataset but without any dummy-encoding
tempdata = tempdata.fillna(0)


mis_val = mydata.isnull().sum()
mydata = mydata.fillna(0)
mydata = pd.get_dummies(mydata, columns =["Given Grade"], prefix = ["V"])


# first attempt at multiple linear regression

trainingSet = tempdata

X = trainingSet[["Number of footholds", "Jugs"]]           

#Y = trainingSet['V_2.0']

Y = trainingSet['Given Grade']
#Y = ['V_0.0', 'V_1.0', 'V_2.0', 'V_3.0']
#testrow = [10, 15.08, 45, 6, 2, 0, 3, 0, 1, 4, 1, 1, 0]
#testrow = [12, 13.25, 0, 13, 0, 0, 12, 0, 0, 0, 0, 0]
testrow1 = [13, 12]
testrow2 = [10, 0]


#gradeList = ['V_0.0', 'V_1.0', 'V_2.0', 'V_3.0']
#predictDict = {}



regr = linear_model.LinearRegression()
regr.fit(X,Y)

predictedGradeV0 = regr.predict([testrow1])
predictedGradeV3 = regr.predict([testrow2])

# https://analyticsindiamag.com/maximum-likelihood-estimation-python-guide/



