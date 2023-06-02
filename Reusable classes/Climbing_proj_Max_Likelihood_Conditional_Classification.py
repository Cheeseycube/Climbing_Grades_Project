# Climbing Grade Project 
# Max Likliehood Conditional Classification
# This is similar to maximumum liklihood classification but it enables the use of more variables

# check independence with chi-squared test of independence, the null is independent
# do this by making the two way table and putting that in a chi-squared calculator

import pandas as pd
import numpy as np
import sys
from matplotlib import pyplot as plt
import Climbing_Grade_Proj_Functions as Functions

class Maximum_Liklihood_Conditional_Classification:
    def __init__(self, _feature_columns, _training_set, _test_set, _category_column):
        self.feature_columns = _feature_columns # list of strings
        self.category_column = _category_column # string
        self.training_set = _training_set # pandas dataframe
        self.test_set = _test_set # pandas dataframe

    def max_liklihood_conditional_classification(self):

        # PROBABILITY OF THE DATA OCCURRING GIVEN EACH CATEGORY
        col_name = self.category_column
        categories = self.training_set.col_name.unique()
        for category in categories:
            ProbData_GivenCategory =


    def ProbData(self, _category):
        probability = 1
        category_df = self.create_subset(_category)
        for column in self.feature_columns:
            test_value = self.test_set.iloc[0][column]
            probability *= category_df[column].value_counts()[test_value] /


    def create_subset(self, _category):
        subset = self.training_set
        for i in self.training_set.index:
            if (self.training_set[self.category_column][i] != _category):
                subset = subset.drop([self.training_set.index[i]])
        return subset


ProbData_GivenV0 = ((V0data["Jugs_binned"].value_counts()[jugInput] / V0_count)
                    * (V0data["Footholds_binned"].value_counts()[footInput] / V0_count)
                    * (V0data["Total_Crimps_Binned"].value_counts()[crimpInput]/ V0_count)
                    * (V0data["Extreme_Crimps_Binned"].value_counts()[extremecrimpInput]/ V0_count))

ProbData_GivenV1 = ((V1data["Jugs_binned"].value_counts()[jugInput] / V1_count)
                    * (V1data["Footholds_binned"].value_counts()[footInput] / V1_count)
                    * (V1data["Total_Crimps_Binned"].value_counts()[crimpInput]/ V1_count)
                    * (V1data["Extreme_Crimps_Binned"].value_counts()[extremecrimpInput]/ V1_count))

ProbData_GivenV2 = ((V2data["Jugs_binned"].value_counts()[jugInput] / V2_count)
                    * (V2data["Footholds_binned"].value_counts()[footInput] / V2_count)
                    * (V2data["Total_Crimps_Binned"].value_counts()[crimpInput]/ V2_count)
                    * (V2data["Extreme_Crimps_Binned"].value_counts()[extremecrimpInput]/ V2_count))

ProbData_GivenV3 = ((V3data["Jugs_binned"].value_counts()[jugInput] / V3_count)
                    * (V3data["Footholds_binned"].value_counts()[footInput] / V3_count)
                    * (V3data["Total_Crimps_Binned"].value_counts()[crimpInput]/ V3_count)
                    * (V3data["Extreme_Crimps_Binned"].value_counts()[extremecrimpInput]/ V3_count))

ProbData_GivenV4 = ((V4data["Jugs_binned"].value_counts()[jugInput] / V4_count)
                    * (V4data["Footholds_binned"].value_counts()[footInput] / V4_count)
                    * (V4data["Total_Crimps_Binned"].value_counts()[crimpInput]/ V4_count)
                    * (V4data["Extreme_Crimps_Binned"].value_counts()[extremecrimpInput]/ V4_count))

ProbData_GivenV7 = ((V7data["Jugs_binned"].value_counts()[jugInput] / V7_count)
                    * (V7data["Footholds_binned"].value_counts()[footInput] / V7_count)
                    * (V7data["Total_Crimps_Binned"].value_counts()[crimpInput]/ V7_count)
                    * (V7data["Extreme_Crimps_Binned"].value_counts()[extremecrimpInput]/ V7_count))

ProbData_GivenV10 = ((V10data["Jugs_binned"].value_counts()[jugInput] / V10_count)
                    * (V10data["Footholds_binned"].value_counts()[footInput] / V10_count)
                    * (V10data["Total_Crimps_Binned"].value_counts()[crimpInput]/ V10_count)
                    * (V10data["Extreme_Crimps_Binned"].value_counts()[extremecrimpInput]/ V10_count))

# PROBABILITY OF EACH GRADE OCCURRING IN GENERAL
total_row_count = len(df.index)
Prob_V0 = V0data["Jugs_binned"].size / total_row_count
Prob_V1 = V1data["Jugs_binned"].size / total_row_count
Prob_V2 = V2data["Jugs_binned"].size / total_row_count
Prob_V3 = V3data["Jugs_binned"].size / total_row_count
Prob_V4 = V4data["Jugs_binned"].size / total_row_count
Prob_V7 = V7data["Jugs_binned"].size / total_row_count
Prob_V10 = V10data["Jugs_binned"].size / total_row_count




GivenData_Divided_By_Alldata = ((ProbData_GivenV0 * len(V0data.index)) + (ProbData_GivenV1 * len(V1data.index)) 
                                + (ProbData_GivenV2 * len(V2data.index)) + (ProbData_GivenV3 * len(V3data.index)) 
                                + (ProbData_GivenV4 * len(V4data.index)) + (ProbData_GivenV7 * len(V7data.index))
                                + (ProbData_GivenV10 * len(V10data.index))) / total_row_count 

#error catching
if GivenData_Divided_By_Alldata == 0:
    print("Insufficient data to estimate this climb's grade, quitting program")
    sys.exit(0)

ProbV0_GivenData = ProbData_GivenV0 * Prob_V0 / GivenData_Divided_By_Alldata
ProbV1_GivenData = ProbData_GivenV1 * Prob_V1 / GivenData_Divided_By_Alldata
ProbV2_GivenData = ProbData_GivenV2 * Prob_V2 / GivenData_Divided_By_Alldata
ProbV3_GivenData = ProbData_GivenV3 * Prob_V3 / GivenData_Divided_By_Alldata
ProbV4_GivenData = ProbData_GivenV4 * Prob_V4 / GivenData_Divided_By_Alldata
ProbV7_GivenData = ProbData_GivenV7 * Prob_V7 / GivenData_Divided_By_Alldata
ProbV10_GivenData = ProbData_GivenV10 * Prob_V10 / GivenData_Divided_By_Alldata


''' USER INTERFACE '''

print("The program gives the following probabilities for each grade:\n")
print(f"V0: {ProbV0_GivenData * 100:.2f}%")
print(f"V1: {ProbV1_GivenData * 100:.2f}%")
print(f"V2: {ProbV2_GivenData * 100:.2f}%")
print(f"V3: {ProbV3_GivenData * 100:.2f}%")
print(f"V4: {ProbV4_GivenData * 100:.2f}%")
print(f"V7: {ProbV7_GivenData * 100:.2f}%")
print(f"V10: {ProbV10_GivenData * 100:.2f}%")
























