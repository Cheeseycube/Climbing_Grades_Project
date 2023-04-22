# Climbing Grade Project
# Functions file
import pandas as pd
import numpy as np

def get_data():
    # IMPORTING AND CLEANING THE DATA
    df = pd.read_excel("Climbing_Stats_ProjectVersion.xlsx")
    tempdata = df
    tempdata = tempdata.fillna(0)    
    mis_val = tempdata.isnull().sum() # this should be empty
    print("missing values: ")
    print(mis_val)
    df = tempdata
    return df

def export_data(df):
    df.to_excel("Climbing_Stats_ProjectVersion.xlsx")
    print("EXPORTED DATA TO EXCEL")



def createV0Data(df):
    V0data = df
    for i in df.index:
        if (df["Given Grade"][i] != 0):
            V0data = V0data.drop([df.index[i]])
    return V0data


def createV1Data(df):
    V1data = df
    for i in df.index:
        if (df["Given Grade"][i] != 1):
            V1data = V1data.drop([df.index[i]])
    return V1data


def createV2Data(df):
    V2data = df
    for i in df.index:
        if (df["Given Grade"][i] != 2):
            V2data = V2data.drop([df.index[i]])
    return V2data


def createV3Data(df):
    V3data = df
    for i in df.index:
        if (df["Given Grade"][i] != 3):
            V3data = V3data.drop([df.index[i]])
    return V3data


def createV4Data(df):
    V4data = df
    for i in df.index:
        if (df["Given Grade"][i] != 4):
            V4data = V4data.drop([df.index[i]])
    return V4data


def createV7Data(df):
    V7data = df
    for i in df.index:
        if (df["Given Grade"][i] != 7):
            V7data = V7data.drop([df.index[i]])
    return V7data


def createV10Data(df):
    V10data = df
    for i in df.index:
        if (df["Given Grade"][i] != 10):
            V10data = V10data.drop([df.index[i]])
    return V10data



if __name__ == "__main__":
    df = get_data()
    print(df.tail())


