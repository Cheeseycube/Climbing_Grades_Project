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
for x in range(25, 29):
    UnencodedData = UnencodedData.drop([mydata.index[x]])
    
#UnencodedData = UnencodedData.drop([mydata.index[17], mydata.index[18]])

mydata = UnencodedData

# this is the same dataset but without any dummy-encoding 
UnencodedData = UnencodedData.fillna(0)


mis_val = mydata.isnull().sum()
mydata = mydata.fillna(0)
mydata = pd.get_dummies(mydata, columns =["Given Grade"], prefix = ["V"])
mydata = pd.get_dummies(mydata, columns = ["Wall angle"], prefix = ["Deg"])

for col in mydata.columns:
    print(col)

# practicing data visualization techniques...

# FOR DUMMY ENCODED VARIABLES
# prints out the number of jugs for each V0
'''
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
 '''
       
# Useful Functions
def createV0Data():
    V0data = UnencodedData
    for i in UnencodedData.index:
        if (UnencodedData["Given Grade"][i] != 0):
            V0data = V0data.drop([UnencodedData.index[i]])
    return V0data

def createV1Data():
    V1data = UnencodedData
    for i in UnencodedData.index:
        if (UnencodedData["Given Grade"][i] != 1):
            V1data = V1data.drop([UnencodedData.index[i]])
    return V1data
            
def createV2Data():
    V2data = UnencodedData
    for i in UnencodedData.index:
        if (UnencodedData["Given Grade"][i] != 2):
            V2data = V2data.drop([UnencodedData.index[i]])
    return V2data

def createV3Data():
    V3data = UnencodedData
    for i in UnencodedData.index:
        if (UnencodedData["Given Grade"][i] != 3):
            V3data = V3data.drop([UnencodedData.index[i]])
    return V3data
            
def createV4Data():
    V4data = UnencodedData
    for i in UnencodedData.index:
        if (UnencodedData["Given Grade"][i] != 4):
            V4data = V4data.drop([UnencodedData.index[i]])
    return V4data

def createEncodedV0Data():
    EncodedV0Data = mydata
    for i in mydata.index:
        if (mydata["V_0.0"][i] != 1):
            EncodedV0Data = EncodedV0Data.drop([mydata.index[i]])
    return EncodedV0Data

# JUG DISTRIBUTION CHARTS

# distribution of jugs for V0s only        
sns.displot(createV0Data(), x="Jugs").set(title = 'Jug Distribution for V0')

# distribution of jugs for V1s only        
sns.displot(createV1Data(), x="Jugs").set(title = 'Jug Distribution for V1')

# distribution of jugs for V2s only        
sns.displot(createV2Data(), x="Jugs").set(title = 'Jug Distribution for V2')

# distribution of jugs for V3s only        
sns.displot(createV3Data(), x="Jugs").set(title = 'Jug Distribution for V3')

# distribution of jugs for V4s only        
sns.displot(createV4Data(), x="Jugs").set(title = 'Jug Distribution for V4')



# NUMBER OF FOOTHOLDS DISTRIBUTION CHARTS

# distribution of Number of footholds for V0s only        
sns.displot(createV0Data(), x="Number of footholds").set(title = 'Foothold distribution for V0')

# distribution of Number of footholds for V1s only        
sns.displot(createV1Data(), x="Number of footholds").set(title = 'Foothold distribution for V1')

# distribution of Number of footholds for V2s only        
sns.displot(createV2Data(), x="Number of footholds").set(title = 'Foothold distribution for V2')

# distribution of Number of footholds for V3s only        
sns.displot(createV3Data(), x="Number of footholds").set(title = 'Foothold distribution for V3')

# distribution of jugs for V4s only        
sns.displot(createV4Data(), x="Number of footholds").set(title = 'Foothold distribution for V4')



#  TOTAL CRIMPS DISTRIBUTION CHARTS

# distribution of Total Crimps for V0s only        
sns.displot(createV0Data(), x="Total Crimps")
plt.title("Total Crimps Distribution for V0", fontsize = 15, color = "red")
plt.ylim(0, 5)
plt.xlim(0, 10)
plt.xlabel("Number of Crimps", fontsize = 20, color = "red")
plt.ylabel("Num. Climbs", fontsize = 20, color = "red")
plt.show()

# distribution of Total Crimps for V1s only        
sns.displot(createV1Data(), x="Total Crimps")
plt.title("Total Crimps Distribution for V1", fontsize = 15, color = "red")
plt.ylim(0, 5)
plt.xlim(0, 10)
plt.xlabel("Number of Crimps", fontsize = 20, color = "red")
plt.ylabel("Num. Climbs", fontsize = 20, color = "red")
plt.show()

# distribution of Total Crimps for V2s only        
sns.displot(createV2Data(), x="Total Crimps")
plt.title("Total Crimps Distribution for V2", fontsize = 15, color = "red")
plt.ylim(0, 5)
plt.xlim(0, 10)
plt.xlabel("Number of Crimps", fontsize = 20, color = "red")
plt.ylabel("Num. Climbs", fontsize = 20, color = "red")
plt.show()

# distribution of Total Crimps for V3s only        
sns.displot(createV3Data(), x="Total Crimps")
plt.title("Total Crimps Distribution for V3", fontsize = 15, color = "red")
plt.ylim(0, 5)
plt.xlim(0, 10)
plt.xlabel("Number of Crimps", fontsize = 20, color = "red")
plt.ylabel("Num. Climbs", fontsize = 20, color = "red")
plt.show()

# distribution of jugs for V4s only        
sns.displot(createV4Data(), x="Total Crimps")
plt.title("Total Crimps Distribution for V4", fontsize = 15, color = "red")
plt.ylim(0, 5)
plt.xlim(0, 10)
plt.xlabel("Number of Crimps", fontsize = 20, color = "red")
plt.ylabel("Num. Climbs", fontsize = 20, color = "red")
plt.show()



# DIFFICULT CRIMPS DISTRIBUTION CHARTS

# distribution of difficult Crimps for V0s only        
sns.displot(createV0Data(), x="difficult crimps")
plt.title("Difficult Crimps Distribution for V0", fontsize = 15, color = "red")
plt.ylim(0, 4)
plt.xlim(0, 4)
plt.xlabel("Number of Difficult Crimps", fontsize = 20, color = "red")
plt.ylabel("Num. Climbs", fontsize = 20, color = "red")
plt.show()

# distribution of difficult Crimps for V1s only        
sns.displot(createV1Data(), x="difficult crimps")
plt.title("Difficult Crimps Distribution for V1", fontsize = 15, color = "red")
plt.ylim(0, 4)
plt.xlim(0, 4)
plt.xlabel("Number of Difficult Crimps", fontsize = 20, color = "red")
plt.ylabel("Num. Climbs", fontsize = 20, color = "red")
plt.show()

# distribution of difficult Crimps for V2s only        
sns.displot(createV2Data(), x="difficult crimps")
plt.title("Difficult Crimps Distribution for V2", fontsize = 15, color = "red")
plt.ylim(0, 4)
plt.xlim(0, 4)
plt.xlabel("Number of Difficult Crimps", fontsize = 20, color = "red")
plt.ylabel("Num. Climbs", fontsize = 20, color = "red")
plt.show()

# distribution of difficult Crimps for V3s only        
sns.displot(createV3Data(), x="difficult crimps")
plt.title("Difficult Crimps Distribution for V3", fontsize = 15, color = "red")
plt.ylim(0, 4)
plt.xlim(0, 4)
plt.xlabel("Number of Difficult Crimps", fontsize = 20, color = "red")
plt.ylabel("Num. Climbs", fontsize = 20, color = "red")
plt.show()

# distribution of difficult crimps for V4s only        
sns.displot(createV4Data(), x="difficult crimps")
plt.title("Difficult Crimps Distribution for V4", fontsize = 15, color = "red")
plt.ylim(0, 4)
plt.xlim(0, 4)
plt.xlabel("Number of Difficult Crimps", fontsize = 20, color = "red")
plt.ylabel("Num. Climbs", fontsize = 20, color = "red")
plt.show()


# WALL ANGLE DISTRIBUTION CHARTS

# distribution of Wall Angle for V0s only        
pd.Series([3, 1, 0, 0, 0], index = [0.0, 15.0, 30.0, 40.0, 45.0]).plot(kind = "bar", title = "Wall Angle distribution for V0", ylim = (0, 3))
plt.show()

# distribution of Wall Angle for V1s only   
pd.Series([1, 2, 0, 1, 2], index = [0.0, 15.0, 30.0, 40.0, 45.0]).plot(kind = "bar", title = "Wall Angle distribution for V1", ylim = (0, 3))
plt.show()

# distribution of Wall Angle for V2s only        
pd.Series([1, 2, 0, 1, 3], index = [0.0, 15.0, 30.0, 40.0, 45.0]).plot(kind = "bar", title = "Wall Angle distribution for V2", ylim = (0, 3))
plt.show()

# distribution of Wall Angle for V3s only        
pd.Series([0, 2, 1, 0, 1], index = [0.0, 15.0, 30.0, 40.0, 45.0]).plot(kind = "bar", title = "Wall Angle distribution for V3", ylim = (0, 3))
plt.show()

# distribution of Wall Angle for V4s only        
pd.Series([0, 1, 0, 0, 1], index = [0.0, 15.0, 30.0, 40.0, 45.0]).plot(kind = "bar", title = "Wall Angle distribution for V4", ylim = (0, 3))
plt.show()



#  OVERALL DISTANCE DISTRIBUTION CHARTS

# distribution of Overall Distance for V0s only      
sns.displot(createV0Data(), x="Overall distance (ft)")
plt.title("Overall Distance Distribution for V0", fontsize = 15, color = "red")
plt.ylim(0, 3)
plt.xlim(5, 20)
plt.xlabel("Distance Per Climb", fontsize = 20, color = "red")
plt.ylabel("Num. Climbs", fontsize = 20, color = "red")
plt.show()

# distribution of Overall Distance for V1s only       
sns.displot(createV1Data(), x="Overall distance (ft)")
plt.title("Overall Distance Distribution for V1", fontsize = 15, color = "red")
plt.ylim(0, 3)
plt.xlim(5, 20)
plt.xlabel("Distance Per Climb", fontsize = 20, color = "red")
plt.ylabel("Num. Climbs", fontsize = 20, color = "red")
plt.show()

# distribution of Overall Distance for V2s only          
sns.displot(createV2Data(), x="Overall distance (ft)")
plt.title("Overall Distance Distribution for V2", fontsize = 15, color = "red")
plt.ylim(0, 3)
plt.xlim(5, 20)
plt.xlabel("Distance Per Climb", fontsize = 20, color = "red")
plt.ylabel("Num. Climbs", fontsize = 20, color = "red")
plt.show()

# distribution of Overall Distance for V3s only        
sns.displot(createV3Data(), x="Overall distance (ft)")
plt.title("Overall Distance Distribution for V3", fontsize = 15, color = "red")
plt.ylim(0, 3)
plt.xlim(5, 20)
plt.xlabel("Distance Per Climb", fontsize = 20, color = "red")
plt.ylabel("Num. Climbs", fontsize = 20, color = "red")
plt.show()

# distribution of Overall Distance for V4s only        
sns.displot(createV4Data(), x="Overall distance (ft)")
plt.title("Overall Distance Distribution for V4", fontsize = 15, color = "red")
plt.ylim(0, 3)
plt.xlim(5, 20)
plt.xlabel("Distance Per Climb", fontsize = 20, color = "red")
plt.ylabel("Num. Climbs", fontsize = 20, color = "red")
plt.show()


# TESTING CODE 

tempvalues = createV3Data()["Wall angle"].value_counts().sort_index()
SeriesToAppend = pd.Series([0,], index = [0.0])
SeriesToAppend.name = 0
tempvalues = tempvalues.append(SeriesToAppend)

createV3Data()["Wall angle"].value_counts().sort_index().append(pd.Series([0, 0, 0], 
                                                                          index = [30.0, 40.0, 45.0])).plot(kind = "bar", 
                                                                                                            title = "Wall Angle distribution for V0")
plt.show()

createV1Data()["Wall angle"].value_counts().sort_index().plot(kind = "bar", title = "Wall Angle distribution for V2")
plt.show()

pd.Series([0, 1, 0, 0, 1], index = [0.0, 15.0, 30.0, 40.0, 45.0]).plot(kind = "bar", title = "Wall Angle distribution for V4", ylim = (0, 4))
plt.show()
