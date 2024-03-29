# Climbing Grade Project
# Data Exploration

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

mydata = pd.read_excel("Climbing_Stats_ProjectVersion.xlsx")

UnencodedData = mydata


    
#UnencodedData = UnencodedData.drop([mydata.index[17], mydata.index[18]])

mydata = UnencodedData

# this is the same dataset but without any dummy-encoding 
UnencodedData = UnencodedData.fillna(0)
UnencodedData["Total Crimps Proportion"] = mydata["Total Crimps"] / mydata["Num. handholds"]

mis_val = mydata.isnull().sum()
mydata = mydata.fillna(0)
mydata = pd.get_dummies(mydata, columns =["Given Grade"], prefix = ["V"])
mydata = pd.get_dummies(mydata, columns = ["Wall angle"], prefix = ["Deg"])


mydata["Total Crimps Proportion"] = mydata["Total Crimps"] / mydata["Num. handholds"]

sns.displot(UnencodedData, x="Given Grade")
plt.title("Grades Distribution", fontsize = 20, color = "red")
plt.xlabel("Given Grade", fontsize = 20, color = "red")
plt.ylabel("Num. Climbs", fontsize = 20, color = "red")
plt.show()
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

def createV7Data():
    V7data = UnencodedData
    for i in UnencodedData.index:
        if (UnencodedData["Given Grade"][i] != 7):
            V7data = V7data.drop([UnencodedData.index[i]])
    return V7data

def createV10Data():
    V10data = UnencodedData
    for i in UnencodedData.index:
        if (UnencodedData["Given Grade"][i] != 10):
            V10data = V10data.drop([UnencodedData.index[i]])
    return V10data

def createEncodedV0Data():
    EncodedV0Data = mydata
    for i in mydata.index:
        if (mydata["V_0.0"][i] != 1):
            EncodedV0Data = EncodedV0Data.drop([mydata.index[i]])
    return EncodedV0Data



# TOTAL CRIMP PROPORTION DISTRIBUTION CHARTS

# distribution for V0s only        
sns.displot(createV0Data(), x="Total Crimps Proportion")
plt.title("Total Crimps Proportion Distribution for V0", fontsize = 15, color = "red")
plt.ylim(0, 4)
plt.xlim(0, 16)
plt.xlabel("Crimp Proportion", fontsize = 20, color = "red")
plt.ylabel("Num. Climbs", fontsize = 20, color = "red")
plt.show()

# distribution for V1s only        
sns.displot(createV1Data(), x="Total Crimps Proportion")
plt.title("Total Crimps Proportion Distribution for V1", fontsize = 15, color = "red")
plt.ylim(0, 4)
plt.xlim(0, 16)
plt.xlabel("Crimp Proportion", fontsize = 20, color = "red")
plt.ylabel("Num. Climbs", fontsize = 20, color = "red")
plt.show()

# distribution for V2s only        
sns.displot(createV2Data(), x="Total Crimps Proportion")
plt.title("Total Crimps Proportion Distribution for V2", fontsize = 15, color = "red")
plt.ylim(0, 4)
plt.xlim(0, 16)
plt.xlabel("Crimp Proportion", fontsize = 20, color = "red")
plt.ylabel("Num. Climbs", fontsize = 20, color = "red")
plt.show()

# distribution for V3s only        
sns.displot(createV3Data(), x="Total Crimps Proportion")
plt.title("Total Crimps Proportion Distribution for V3", fontsize = 15, color = "red")
plt.ylim(0, 4)
plt.xlim(0, 16)
plt.xlabel("Crimp Proportion", fontsize = 20, color = "red")
plt.ylabel("Num. Climbs", fontsize = 20, color = "red")
plt.show()

# distribution for V4s only        
sns.displot(createV4Data(), x="Total Crimps Proportion")
plt.title("Total Crimps Proportion Distribution for V4", fontsize = 15, color = "red")
plt.ylim(0, 4)
plt.xlim(0, 16)
plt.xlabel("Crimp Proportion", fontsize = 20, color = "red")
plt.ylabel("Num. Climbs", fontsize = 20, color = "red")
plt.show()




# JUG DISTRIBUTION CHARTS

# distribution of jugs for V0s only        
sns.displot(createV0Data(), x="Jugs")
plt.title("Jugs Distribution for V0", fontsize = 15, color = "red")
plt.ylim(0, 4)
plt.xlim(0, 16)
plt.xlabel("Number of Jugs", fontsize = 20, color = "red")
plt.ylabel("Num. Climbs", fontsize = 20, color = "red")
plt.show()

# distribution of jugs for V1s only        
sns.displot(createV1Data(), x="Jugs")
plt.title("Jugs Distribution for V1", fontsize = 15, color = "red")
plt.ylim(0, 4)
plt.xlim(0, 16)
plt.xlabel("Number of Jugs", fontsize = 20, color = "red")
plt.ylabel("Num. Climbs", fontsize = 20, color = "red")
plt.show()

# distribution of jugs for V2s only        
sns.displot(createV2Data(), x="Jugs")
plt.title("Jugs Distribution for V2", fontsize = 15, color = "red")
plt.ylim(0, 4)
plt.xlim(0, 16)
plt.xlabel("Number of Jugs", fontsize = 20, color = "red")
plt.ylabel("Num. Climbs", fontsize = 20, color = "red")
plt.show()

# distribution of jugs for V3s only        
sns.displot(createV3Data(), x="Jugs")
plt.title("Jugs Distribution for V3", fontsize = 15, color = "red")
plt.ylim(0, 4)
plt.xlim(0, 16)
plt.xlabel("Number of Jugs", fontsize = 20, color = "red")
plt.ylabel("Num. Climbs", fontsize = 20, color = "red")
plt.show()

# distribution of jugs for V4s only        
sns.displot(createV4Data(), x="Jugs")
plt.title("Jugs Distribution for V4", fontsize = 15, color = "red")
plt.ylim(0, 4)
plt.xlim(0, 16)
plt.xlabel("Number of Jugs", fontsize = 20, color = "red")
plt.ylabel("Num. Climbs", fontsize = 20, color = "red")
plt.show()



# NUMBER OF FOOTHOLDS DISTRIBUTION CHARTS

# distribution of Number of footholds for V0s only        
sns.displot(createV0Data(), x="Number of footholds")
plt.title("Foothold Distribution for V0", fontsize = 15, color = "red")
plt.ylim(0, 3)
plt.xlim(0, 14)
plt.xlabel("Number of Jugs", fontsize = 20, color = "red")
plt.ylabel("Num. Climbs", fontsize = 20, color = "red")
plt.show()

# distribution of Number of footholds for V1s only        
sns.displot(createV1Data(), x="Number of footholds")
plt.title("Foothold Distribution for V1", fontsize = 15, color = "red")
plt.ylim(0, 3)
plt.xlim(0, 14)
plt.xlabel("Number of Jugs", fontsize = 20, color = "red")
plt.ylabel("Num. Climbs", fontsize = 20, color = "red")
plt.show()

# distribution of Number of footholds for V2s only        
sns.displot(createV2Data(), x="Number of footholds")
plt.title("Foothold Distribution for V2", fontsize = 15, color = "red")
plt.ylim(0, 3)
plt.xlim(0, 14)
plt.xlabel("Number of Jugs", fontsize = 20, color = "red")
plt.ylabel("Num. Climbs", fontsize = 20, color = "red")
plt.show()

# distribution of Number of footholds for V3s only        
sns.displot(createV3Data(), x="Number of footholds")
plt.title("Foothold Distribution for V3", fontsize = 15, color = "red")
plt.ylim(0, 3)
plt.xlim(0, 14)
plt.xlabel("Number of Jugs", fontsize = 20, color = "red")
plt.ylabel("Num. Climbs", fontsize = 20, color = "red")
plt.show()

# distribution of jugs for V4s only        
sns.displot(createV4Data(), x="Number of footholds")
plt.title("Foothold Distribution for V4", fontsize = 15, color = "red")
plt.ylim(0, 3)
plt.xlim(0, 14)
plt.xlabel("Number of Jugs", fontsize = 20, color = "red")
plt.ylabel("Num. Climbs", fontsize = 20, color = "red")
plt.show()



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
plt.ylim(0, 6)
plt.xlim(0, 5)
plt.xlabel("Number of Difficult Crimps", fontsize = 20, color = "red")
plt.ylabel("Num. Climbs", fontsize = 20, color = "red")
plt.show()

# distribution of difficult Crimps for V1s only        
sns.displot(createV1Data(), x="difficult crimps")
plt.title("Difficult Crimps Distribution for V1", fontsize = 15, color = "red")
plt.ylim(0, 6)
plt.xlim(0, 5)
plt.xlabel("Number of Difficult Crimps", fontsize = 20, color = "red")
plt.ylabel("Num. Climbs", fontsize = 20, color = "red")
plt.show()

# distribution of difficult Crimps for V2s only        
sns.displot(createV2Data(), x="difficult crimps")
plt.title("Difficult Crimps Distribution for V2", fontsize = 15, color = "red")
plt.ylim(0, 6)
plt.xlim(0, 5)
plt.xlabel("Number of Difficult Crimps", fontsize = 20, color = "red")
plt.ylabel("Num. Climbs", fontsize = 20, color = "red")
plt.show()

# distribution of difficult Crimps for V3s only        
sns.displot(createV3Data(), x="difficult crimps")
plt.title("Difficult Crimps Distribution for V3", fontsize = 15, color = "red")
plt.ylim(0, 6)
plt.xlim(0, 5)
plt.xlabel("Number of Difficult Crimps", fontsize = 20, color = "red")
plt.ylabel("Num. Climbs", fontsize = 20, color = "red")
plt.show()

# distribution of difficult crimps for V4s only        
sns.displot(createV4Data(), x="difficult crimps")
plt.title("Difficult Crimps Distribution for V4", fontsize = 15, color = "red")
plt.ylim(0, 6)
plt.xlim(0, 5)
plt.xlabel("Number of Difficult Crimps", fontsize = 20, color = "red")
plt.ylabel("Num. Climbs", fontsize = 20, color = "red")
plt.show()

# distribution of difficult crimps for V7s only        
sns.displot(createV7Data(), x="difficult crimps")
plt.title("Difficult Crimps Distribution for V7", fontsize = 15, color = "red")
plt.ylim(0, 6)
plt.xlim(0, 5)
plt.xlabel("Number of Difficult Crimps", fontsize = 20, color = "red")
plt.ylabel("Num. Climbs", fontsize = 20, color = "red")
plt.show()

# distribution of difficult crimps for V10s only        
sns.displot(createV10Data(), x="difficult crimps")
plt.title("Difficult Crimps Distribution for V10", fontsize = 15, color = "red")
plt.ylim(0, 6)
plt.xlim(0, 5)
plt.xlabel("Number of Difficult Crimps", fontsize = 20, color = "red")
plt.ylabel("Num. Climbs", fontsize = 20, color = "red")
plt.show()



# EXTREME CRIMPS DISTRIBUTION CHARTS

# distribution of extreme Crimps for V0s only        
sns.displot(createV0Data(), x="extreme crimps")
plt.title("Extreme Crimps Distribution for V0", fontsize = 15, color = "red")
plt.ylim(0, 7)
plt.xlim(0, 3)
plt.xlabel("Number of Difficult Crimps", fontsize = 20, color = "red")
plt.ylabel("Num. Climbs", fontsize = 20, color = "red")
plt.show()

# distribution of extreme Crimps for V1s only        
sns.displot(createV1Data(), x="extreme crimps")
plt.title("Extreme Crimps Distribution for V1", fontsize = 15, color = "red")
plt.ylim(0, 7)
plt.xlim(0, 3)
plt.xlabel("Number of Difficult Crimps", fontsize = 20, color = "red")
plt.ylabel("Num. Climbs", fontsize = 20, color = "red")
plt.show()

# distribution of extreme Crimps for V2s only        
sns.displot(createV2Data(), x="extreme crimps")
plt.title("Extreme Crimps Distribution for V2", fontsize = 15, color = "red")
plt.ylim(0, 7)
plt.xlim(0, 3)
plt.xlabel("Number of Difficult Crimps", fontsize = 20, color = "red")
plt.ylabel("Num. Climbs", fontsize = 20, color = "red")
plt.show()

# distribution of extreme Crimps for V3s only        
sns.displot(createV3Data(), x="extreme crimps")
plt.title("Extreme Crimps Distribution for V3", fontsize = 15, color = "red")
plt.ylim(0, 7)
plt.xlim(0, 3)
plt.xlabel("Number of Difficult Crimps", fontsize = 20, color = "red")
plt.ylabel("Num. Climbs", fontsize = 20, color = "red")
plt.show()

# distribution of extreme crimps for V4s only        
sns.displot(createV4Data(), x="extreme crimps")
plt.title("Extreme Crimps Distribution for V4", fontsize = 15, color = "red")
plt.ylim(0, 7)
plt.xlim(0, 3)
plt.xlabel("Number of Difficult Crimps", fontsize = 20, color = "red")
plt.ylabel("Num. Climbs", fontsize = 20, color = "red")
plt.show()

# distribution of extreme crimps for V7s only        
sns.displot(createV7Data(), x="extreme crimps")
plt.title("Extreme Crimps Distribution for V7", fontsize = 15, color = "red")
plt.ylim(0, 7)
plt.xlim(0, 3)
plt.xlabel("Number of Difficult Crimps", fontsize = 20, color = "red")
plt.ylabel("Num. Climbs", fontsize = 20, color = "red")
plt.show()

# distribution of extreme crimps for V10s only        
sns.displot(createV10Data(), x="extreme crimps")
plt.title("Extreme Crimps Distribution for V10", fontsize = 15, color = "red")
plt.ylim(0, 7)
plt.xlim(0, 3)
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

#DistancePlot = UnencodedData.plot.scatter(x='Overall distance (ft)',
#                       y='Given Grade', c='DarkBlue')

# TESTING CODE 


