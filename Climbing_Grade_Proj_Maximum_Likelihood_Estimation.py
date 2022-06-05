# Climbing Grade Project
# Maximum Likelihood Estimation

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import minimize
import scipy.stats as stats
import seaborn as sns

import pymc3 as pm3
import numdifftools as ndt
import statsmodels.api as sm
from statsmodels.base.model import GenericLikelihoodModel

# this is only useful for jupyter notebooks as far as I can tell
#%matplotlib inline

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



# 2 way table for V0:  number of jugs and number of footholds  

V0data = tempdata
for i in tempdata.index:
    if (tempdata["Given Grade"][i] != 0):
        V0data = V0data.drop([tempdata.index[i]])
        
V0_table = pd.crosstab(index = V0data["Number of footholds"],
                       columns = V0data["Jugs"])

#V0_table = sns.heatmap(pd.crosstab(index = V0data["Number of footholds"],
#                       columns = V0data["Jugs"]))


#BREAK

# 2 way table for V1: number of jugs and number of footholds

V1data = tempdata
for i in tempdata.index:
    if (tempdata["Given Grade"][i] != 1):
        V1data = V1data.drop([tempdata.index[i]])
        
V1_table = pd.crosstab(index = V1data["Number of footholds"],
                       columns = V1data["Jugs"])


V2data = tempdata
for i in tempdata.index:
    if (tempdata["Given Grade"][i] != 2):
        V2data = V2data.drop([tempdata.index[i]])
        
V2_table = pd.crosstab(index = V2data["Number of footholds"],
                       columns = V2data["Jugs"])

V3data = tempdata
for i in tempdata.index:
    if (tempdata["Given Grade"][i] != 3):
        V3data = V3data.drop([tempdata.index[i]])
        
V3_table = pd.crosstab(index = V3data["Number of footholds"],
                       columns = V3data["Jugs"])


try:
    ProbGivenData_V0 = V0_table.at[8,11] / V0data["Jugs"].size   # Probability the given data is a v0
except:
    ProbGivenData_V0 = 0
Prob_V0 = V0data["Jugs"].size / mydata["Jugs"].size          # Probability that a climb is v0

try:
    ProbGivenData_V1 = V1_table.at[8,11] / V1data["Jugs"].size   # Probability the given data is a v1
except:
    ProbGivenData_V1 = 0
Prob_V1 = V1data["Jugs"].size / mydata["Jugs"].size          # Probability that a climb is v1
 
try:
    ProbGivenData_V2 = V2_table.at[8,11] / V2data["Jugs"].size   # Probability the given data is a v2
except:
    ProbGivenData_V2 = 0    
Prob_V2 = V2data["Jugs"].size / mydata["Jugs"].size          # Probability that a climb is v2

try:
    ProbGivenData_V3 = V3_table.at[8,11] / V3data["Jugs"].size   # Probability the given data is a v3
except:
    ProbGivenData_V3 = 0
Prob_V3 = V3data["Jugs"].size / mydata["Jugs"].size          # Probability that a climb is v3


GivenData_Divided_By_Alldata = ((ProbGivenData_V0 * V0data["Jugs"].size) + (ProbGivenData_V1 * V1data["Jugs"].size) 
+ (ProbGivenData_V2 * V2data["Jugs"].size) + (ProbGivenData_V3 * V3data["Jugs"].size)) / mydata["Jugs"].size 

ProbV0_GivenData = ProbGivenData_V0 * Prob_V0 / GivenData_Divided_By_Alldata

ProbV1_GivenData = ProbGivenData_V1 * Prob_V1 / GivenData_Divided_By_Alldata

ProbV2_GivenData = ProbGivenData_V2 * Prob_V2 / GivenData_Divided_By_Alldata

ProbV3_GivenData = ProbGivenData_V3 * Prob_V3 / GivenData_Divided_By_Alldata
