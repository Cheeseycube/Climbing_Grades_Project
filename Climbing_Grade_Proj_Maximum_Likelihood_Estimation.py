# Climbing Grade Project
# Maximum Likelihood Estimation

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import minimize
import scipy.stats as stats
import seaborn as sns


# this is only useful for jupyter notebooks as far as I can tell
#%matplotlib inline

mydata = pd.read_excel("Climbing_Stats_ProjectVersion.xlsx")


mydata = mydata.drop('Observations', 1) # Dropping the observations column. 1 for cols, 0 for rows
mydata = mydata.drop('Size of holds', 1)
mydata = mydata.drop('Distance between holds for intended beta', 1)

# REMOVES V4 V7 and V10 FROM THE DATASET
tempdata = mydata
for i in tempdata.index:
    if (tempdata["Given Grade"][i] == 4):
        mydata = mydata.drop([tempdata.index[i]])

for i in tempdata.index:
    if (tempdata["Given Grade"][i] == 7):
        mydata = mydata.drop([tempdata.index[i]])
        
for i in tempdata.index:
    if (tempdata["Given Grade"][i] == 10):
        mydata = mydata.drop([tempdata.index[i]])
        

    
UnencodedData = mydata


# update the below code if removing v4 v7 v10

# dropping empty rows at the bottom   This works by checking each index in the original dataset, then removing that specific row from the new dataset regardless of index
# first argument is row to start on, second is one over the row to end on
for x in range(25, 29):
    UnencodedData = UnencodedData.drop([mydata.index[x]])
    
#UnencodedData = UnencodedData.drop([mydata.index[17], mydata.index[18]])

mydata = UnencodedData

# this is the same dataset but without any dummy-encoding
UnencodedData = UnencodedData.fillna(0)


mis_val = mydata.isnull().sum()
mydata = mydata.fillna(0)
mydata = pd.get_dummies(mydata, columns =["Given Grade"], prefix = ["V"])





# 2 way table for V0:  number of jugs and number of footholds  

V0data = UnencodedData
for i in UnencodedData.index:
    if (UnencodedData["Given Grade"][i] != 0):
        V0data = V0data.drop([UnencodedData.index[i]])
        
V0_table = pd.crosstab(index = V0data["Number of footholds"],
                       columns = V0data["Jugs"])

#V0_table = sns.heatmap(pd.crosstab(index = V0data["Number of footholds"],
#                       columns = V0data["Jugs"]))


#BREAK

# 2 way table for V1: number of jugs and number of footholds

V1data = UnencodedData
for i in UnencodedData.index:
    if (UnencodedData["Given Grade"][i] != 1):
        V1data = V1data.drop([UnencodedData.index[i]])
        
V1_table = pd.crosstab(index = V1data["Number of footholds"],
                       columns = V1data["Jugs"])


V2data = UnencodedData
for i in UnencodedData.index:
    if (UnencodedData["Given Grade"][i] != 2):
        V2data = V2data.drop([UnencodedData.index[i]])
        
V2_table = pd.crosstab(index = V2data["Number of footholds"],
                       columns = V2data["Jugs"])

V3data = UnencodedData
for i in UnencodedData.index:
    if (UnencodedData["Given Grade"][i] != 3):
        V3data = V3data.drop([UnencodedData.index[i]])
        
V3_table = pd.crosstab(index = V3data["Number of footholds"],
                       columns = V3data["Jugs"])


try:
    ProbData_GivenV0 = V0_table.at[8,11] / V0data["Jugs"].size   # Probability of the data given a v0
except:
    ProbData_GivenV0 = 0
Prob_V0 = V0data["Jugs"].size / UnencodedData["Jugs"].size          # Probability that a climb is v0

try:
    ProbData_GivenV1 = V1_table.at[8,11] / V1data["Jugs"].size   # Probability of the data given a v1
except:
    ProbData_GivenV1 = 0
Prob_V1 = V1data["Jugs"].size / UnencodedData["Jugs"].size          # Probability that a climb is v1
 
try:
    ProbData_GivenV2 = V2_table.at[8,11] / V2data["Jugs"].size   # Probability of the data given a v2
except:
    ProbData_GivenV2 = 0    
Prob_V2 = V2data["Jugs"].size / UnencodedData["Jugs"].size          # Probability that a climb is v2

try:
    ProbData_GivenV3 = V3_table.at[8,11] / V3data["Jugs"].size   # Probability of the data given a v3
except:
    ProbData_GivenV3 = 0
Prob_V3 = V3data["Jugs"].size / UnencodedData["Jugs"].size          # Probability that a climb is v3


GivenData_Divided_By_Alldata = ((ProbData_GivenV0 * V0data["Jugs"].size) + (ProbData_GivenV1 * V1data["Jugs"].size) 
+ (ProbData_GivenV2 * V2data["Jugs"].size) + (ProbData_GivenV3 * V3data["Jugs"].size)) / mydata["Jugs"].size 

ProbV0_GivenData = ProbData_GivenV0 * Prob_V0 / GivenData_Divided_By_Alldata

ProbV1_GivenData = ProbData_GivenV1 * Prob_V1 / GivenData_Divided_By_Alldata

ProbV2_GivenData = ProbData_GivenV2 * Prob_V2 / GivenData_Divided_By_Alldata

ProbV3_GivenData = ProbData_GivenV3 * Prob_V3 / GivenData_Divided_By_Alldata



# SAME STUFF BUT WITH BINNED DATA (Num. Jugs and Num. Footholds)

# Binning Jugs
min_value = UnencodedData['Jugs'].min()
max_value = UnencodedData['Jugs'].max()

bins = np.linspace(min_value, max_value, 4)
labels = ['small', 'medium', 'big']
UnencodedData['Jugs_binned'] = pd.cut(UnencodedData['Jugs'], bins = bins, labels = labels, include_lowest = True)

plt.hist(UnencodedData['Jugs_binned'], bins = 3)


# Binning Footholds
min_value = UnencodedData['Number of footholds'].min()
max_value = UnencodedData['Number of footholds'].max()

bins = np.linspace(min_value, max_value, 4)
labels = ['small', 'medium', 'big']
UnencodedData['Footholds_binned'] = pd.cut(UnencodedData['Number of footholds'], bins = bins, labels = labels, include_lowest = True)

plt.hist(UnencodedData['Footholds_binned'], bins = 3)


# SAME AS ABOVE

# 2 way table for V0:  number of jugs and number of footholds  

Jugs_Binned = "Jugs_binned"
Footholds_Binned = "Footholds_binned"
V0data = UnencodedData
for i in UnencodedData.index:
    if (UnencodedData["Given Grade"][i] != 0):
        V0data = V0data.drop([UnencodedData.index[i]])
        
V0_table = pd.crosstab(index = V0data[Footholds_Binned],
                       columns = V0data[Jugs_Binned])

#V0_table = sns.heatmap(pd.crosstab(index = V0data["Number of footholds"],
#                       columns = V0data["Jugs"]))


#BREAK

# 2 way table for V1: number of jugs and number of footholds

V1data = UnencodedData
for i in UnencodedData.index:
    if (UnencodedData["Given Grade"][i] != 1):
        V1data = V1data.drop([UnencodedData.index[i]])
        
V1_table = pd.crosstab(index = V1data[Footholds_Binned],
                       columns = V1data[Jugs_Binned])


V2data = UnencodedData
for i in UnencodedData.index:
    if (UnencodedData["Given Grade"][i] != 2):
        V2data = V2data.drop([UnencodedData.index[i]])
        
V2_table = pd.crosstab(index = V2data[Footholds_Binned],
                       columns = V2data[Jugs_Binned])

V3data = UnencodedData
for i in UnencodedData.index:
    if (UnencodedData["Given Grade"][i] != 3):
        V3data = V3data.drop([UnencodedData.index[i]])
        
V3_table = pd.crosstab(index = V3data[Footholds_Binned],
                       columns = V3data[Jugs_Binned])

# footholds, jugs
try:
    ProbData_GivenV0 = V0_table.at['small','small'] / V0data[Jugs_Binned].size   # Probability of the data given a v0
except:
    ProbData_GivenV0 = 0 # sets the probability to 0 if no data is found
Prob_V0 = V0data[Jugs_Binned].size / UnencodedData[Jugs_Binned].size          # Probability that a climb is v0

try:
    ProbData_GivenV1 = V1_table.at['small','small'] / V1data[Jugs_Binned].size   # Probability of the data given a v1
except:
    ProbData_GivenV1 = 0 # sets the probability to 0 if no data is found
Prob_V1 = V1data[Jugs_Binned].size / UnencodedData[Jugs_Binned].size          # Probability that a climb is v1
 
try:
    ProbData_GivenV2 = V2_table.at['small','small'] / V2data[Jugs_Binned].size   # Probability of the data given a v2
except:
    ProbData_GivenV2 = 0 # sets the probability to 0 if no data is found
Prob_V2 = V2data[Jugs_Binned].size / UnencodedData[Jugs_Binned].size          # Probability that a climb is v2

try:
    ProbData_GivenV3 = V3_table.at['small','small'] / V3data[Jugs_Binned].size   # Probability of the data given a v3
except:
    ProbData_GivenV3 = 0 # sets the probability to 0 if no data is found
Prob_V3 = V3data[Jugs_Binned].size / UnencodedData[Jugs_Binned].size          # Probability that a climb is v3


GivenData_Divided_By_Alldata = ((ProbData_GivenV0 * V0data[Jugs_Binned].size) + (ProbData_GivenV1 * V1data[Jugs_Binned].size) 
+ (ProbData_GivenV2 * V2data[Jugs_Binned].size) + (ProbData_GivenV3 * V3data[Jugs_Binned].size)) / UnencodedData[Jugs_Binned].size 

ProbV0_GivenData = ProbData_GivenV0 * Prob_V0 / GivenData_Divided_By_Alldata

ProbV1_GivenData = ProbData_GivenV1 * Prob_V1 / GivenData_Divided_By_Alldata

ProbV2_GivenData = ProbData_GivenV2 * Prob_V2 / GivenData_Divided_By_Alldata

ProbV3_GivenData = ProbData_GivenV3 * Prob_V3 / GivenData_Divided_By_Alldata




# Num. Jugs and Total Crimps BINNED MAX LIKLIEHOOD

# Binning Jugs
min_value = UnencodedData['Jugs'].min()
max_value = UnencodedData['Jugs'].max()

bins = np.linspace(min_value, max_value, 4)
labels = ['small', 'medium', 'big']
UnencodedData['Jugs_binned'] = pd.cut(UnencodedData['Jugs'], bins = bins, labels = labels, include_lowest = True)

plt.hist(UnencodedData['Jugs_binned'], bins = 3)


# Binning total crimps
min_value = UnencodedData['Total Crimps'].min()
max_value = UnencodedData['Total Crimps'].max()

bins = np.linspace(min_value, max_value, 4)
labels = ['small', 'medium', 'big']
UnencodedData['Total_Crimps_Binned'] = pd.cut(UnencodedData['Total Crimps'], bins = bins, labels = labels, include_lowest = True)

plt.hist(UnencodedData['Total_Crimps_Binned'], bins = 3)




# 2 way table for V0:  number of jugs and total crimps 

Jugs_Binned = "Jugs_binned"
Crimps_Binned = "Total_Crimps_Binned"
V0data = UnencodedData
for i in UnencodedData.index:
    if (UnencodedData["Given Grade"][i] != 0):
        V0data = V0data.drop([UnencodedData.index[i]])
        
V0_table = pd.crosstab(index = V0data[Crimps_Binned],
                       columns = V0data[Jugs_Binned])


#BREAK

# 2 way table for V1: number of jugs and total crimps

V1data = UnencodedData
for i in UnencodedData.index:
    if (UnencodedData["Given Grade"][i] != 1):
        V1data = V1data.drop([UnencodedData.index[i]])
        
V1_table = pd.crosstab(index = V1data[Crimps_Binned],
                       columns = V1data[Jugs_Binned])


V2data = UnencodedData
for i in UnencodedData.index:
    if (UnencodedData["Given Grade"][i] != 2):
        V2data = V2data.drop([UnencodedData.index[i]])
        
V2_table = pd.crosstab(index = V2data[Crimps_Binned],
                       columns = V2data[Jugs_Binned])

V3data = UnencodedData
for i in UnencodedData.index:
    if (UnencodedData["Given Grade"][i] != 3):
        V3data = V3data.drop([UnencodedData.index[i]])
        
V3_table = pd.crosstab(index = V3data[Crimps_Binned],
                       columns = V3data[Jugs_Binned])

# total crimps, total jugs
try:
    ProbData_GivenV0 = V0_table.at['small','small'] / V0data[Jugs_Binned].size   # Probability of the data given a v0
except:
    ProbData_GivenV0 = 0
Prob_V0 = V0data[Jugs_Binned].size / UnencodedData[Jugs_Binned].size          # Probability that a climb is v0

try:
    ProbData_GivenV1 = V1_table.at['small','small'] / V1data[Jugs_Binned].size   # Probability of the data given a v1
except:
    ProbData_GivenV1 = 0
Prob_V1 = V1data[Jugs_Binned].size / UnencodedData[Jugs_Binned].size          # Probability that a climb is v1
 
try:
    ProbData_GivenV2 = V2_table.at['small','small'] / V2data[Jugs_Binned].size   # Probability of the data given a v2
except:
    ProbData_GivenV2 = 0    
Prob_V2 = V2data[Jugs_Binned].size / UnencodedData[Jugs_Binned].size          # Probability that a climb is v2

try:
    ProbData_GivenV3 = V3_table.at['small','small'] / V3data[Jugs_Binned].size   # Probability of the data given a v3
except:
    ProbData_GivenV3 = 0
Prob_V3 = V3data[Jugs_Binned].size / UnencodedData[Jugs_Binned].size          # Probability that a climb is v3


GivenData_Divided_By_Alldata = ((ProbData_GivenV0 * V0data[Jugs_Binned].size) + (ProbData_GivenV1 * V1data[Jugs_Binned].size) 
+ (ProbData_GivenV2 * V2data[Jugs_Binned].size) + (ProbData_GivenV3 * V3data[Jugs_Binned].size)) / UnencodedData[Jugs_Binned].size 

ProbV0_GivenData = ProbData_GivenV0 * Prob_V0 / GivenData_Divided_By_Alldata

ProbV1_GivenData = ProbData_GivenV1 * Prob_V1 / GivenData_Divided_By_Alldata

ProbV2_GivenData = ProbData_GivenV2 * Prob_V2 / GivenData_Divided_By_Alldata

ProbV3_GivenData = ProbData_GivenV3 * Prob_V3 / GivenData_Divided_By_Alldata





# prob_num_Jugs_GivenV0 * prob_numCrimps_GivenV0 * prob_numFootholds_GivenV0 = probData_GivenV0
# check independence with chi-squared test of independence, the null is independent