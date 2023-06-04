import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import Climbing_Grade_Proj_Functions as Functions
import Generalized_Max_Likelihood_Conditional_Classification as mlcc





if __name__ == "__main__":

    # GETTING THE DATA
    df = Functions.get_data()

    # Binning Jugs
    min_value = df['Jugs_Category_1'].min()
    max_value = df['Jugs_Category_1'].max()
    JugBins = np.linspace(min_value, max_value, 4)
    labels = ['small', 'medium', 'big']
    df['Jugs_binned'] = pd.cut(df['Jugs_Category_1'], bins=JugBins, labels=labels, include_lowest=True)
    df["Jugs_binned"].value_counts().sort_index().plot(kind="bar", title="Binned Jugs Distribution")
    plt.show()

    # Binning Footholds
    min_value = df['Total Footholds'].min()
    max_value = df['Total Footholds'].max()
    FootholdBins = np.linspace(min_value, max_value, 4)
    labels = ['small', 'medium', 'big']
    df['Footholds_binned'] = pd.cut(df['Total Footholds'], bins=FootholdBins, labels=labels, include_lowest=True)
    df["Footholds_binned"].value_counts().sort_index().plot(kind="bar", title="Binned Footholds Distribution")
    plt.show()

    # Binning total crimps
    min_value = df['Total Crimps'].min()
    max_value = df['Total Crimps'].max()
    TotalCrimpsBins = np.linspace(min_value, max_value, 4)
    labels = ['small', 'medium', 'big']
    df['Total_Crimps_Binned'] = pd.cut(df['Total Crimps'], bins=TotalCrimpsBins, labels=labels, include_lowest=True)
    df["Total_Crimps_Binned"].value_counts().sort_index().plot(kind="bar", title="Binned Total Crimps Distribution")
    plt.show()

    # Binning Crimps_Category_4
    min_value = df['Crimps_Category_4'].min()
    max_value = df['Crimps_Category_4'].max()
    ExtremeCrimpsBins = np.linspace(min_value, max_value, 3)
    labels = ['small', 'big']
    df['Extreme_Crimps_Binned'] = pd.cut(df['Crimps_Category_4'], bins=ExtremeCrimpsBins, labels=labels,
                                         include_lowest=True)
    df["Extreme_Crimps_Binned"].value_counts().sort_index().plot(kind="bar",
                                                                 title="Binned Crimps_Category_4 Distribution")
    plt.show()

    ''' USER INTERFACE BEGIN'''
    print()
    print("Welcome to my experimental Climbing Grade Program!")
    print("If you provide the following measurements for a climb this program will attempt to predict the grade:")
    print("Number of Jugs, Total Footholds, Number of Crimps (any size), Number of Crimps_Category_4")

    numJugs = int(input("Please provide the number of jugs here:\n"))
    jugInput = ""
    if numJugs in range(0, 6):
        print(f"{numJugs} is a small amount of jugs")
        jugInput = "small"

    elif numJugs in range(6, 11):
        print(f"{numJugs} is a medium amount of jugs")
        jugInput = "medium"

    else:
        print(f"{numJugs} is a large amount of jugs")
        jugInput = "big"

    numFootholds = int(input("Please provide the Total Footholds here:\n"))
    footInput = ""
    if numFootholds in range(0, 8):
        print(f"{numFootholds} is a small amount of footholds")
        footInput = "small"

    elif numFootholds in range(8, 15):
        print(f"{numFootholds} is a medium amount of footholds")
        footInput = "medium"

    else:
        print(f"{numFootholds} is a large amount of footholds")
        footInput = "big"

    numCrimps = int(input("Please provide the number of crimps here:\n"))
    crimpInput = ""
    if numCrimps in range(0, 4):
        print(f"{numCrimps} is a small amount of crimps")
        crimpInput = "small"

    elif numCrimps in range(4, 8):
        print(f"{numCrimps} is a medium amount of crimps")
        crimpInput = "medium"

    else:
        print(f"{numCrimps} is a large amount of crimps")
        crimpInput = "big"

    numExtremeCrimps = int(input("Please provide the number of Crimps_Category_4 here:\n"))
    extremecrimpInput = ""
    if numExtremeCrimps in range(0, 1):  # change this threshold if I don't want every extreme crimp to be automatic v10
        print(f"{numExtremeCrimps} is a small amount of Crimps_Category_4")
        extremecrimpInput = "small"

    else:
        print(f"{numExtremeCrimps} is a large amount of Crimps_Category_4")
        extremecrimpInput = "big"

    ''' USER INTERFACE END'''

    features = ["Footholds_binned", "Total_Crimps_Binned", "Extreme_Crimps_Binned", "Jugs_binned"]
    test_dict = {'Footholds_binned': [footInput], 'Total_Crimps_Binned': [crimpInput],
                 'Extreme_Crimps_Binned': [extremecrimpInput], 'Jugs_binned': [jugInput]}
    test_df = pd.DataFrame.from_dict(test_dict)
    model = mlcc.Maximum_Liklihood_Conditional_Classification(_feature_columns=features, _training_set=df, _test_set=test_df,
                                                              _category_column="Grade")
    model.max_liklihood_conditional_classification()

