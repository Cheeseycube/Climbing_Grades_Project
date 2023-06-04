# Generic implementation
# Max Likliehood Conditional Classification
# This is similar to maximumum liklihood classification but it enables the use of more variables

# check independence with chi-squared test of independence, the null is independent
# do this by making the two way table and putting that in a chi-squared calculator

import sys


class Maximum_Liklihood_Conditional_Classification:
    def __init__(self, _feature_columns, _training_set, _test_set, _category_column):
        self.feature_columns = _feature_columns  # list of strings
        self.category_column = _category_column  # string
        self.training_set = _training_set  # pandas dataframe
        self.test_set = _test_set  # pandas dataframe

    # creates a subset of the training set that includes only a given category
    def create_subset(self, _category):
        subset = self.training_set
        for i in self.training_set.index:
            if (self.training_set[self.category_column][i] != _category):
                subset = subset.drop([self.training_set.index[i]])
        return subset

    # Calculates the probability of the test data occurring given each category
    def ProbData_GivenCategory(self, _category):
        probability = 1
        category_df = self.create_subset(_category)
        category_df_length = len(category_df.index)
        for column in self.feature_columns:
            # test_value is the cell in the first row of the test set at the given column
            test_value = self.test_set.iloc[0][column]
            probability *= (category_df[column].value_counts()[test_value] / category_df_length)
        return probability

    # Calculates the probability of the test data falling into each category
    # i.e. the probability of each category occuring given the test data
    def ProbCategory_GivenData(self, Prob_GivenCategory, GivenData_Divided_By_Alldata, category):
        return self.ProbData_GivenCategory(category) * Prob_GivenCategory / GivenData_Divided_By_Alldata

    # maximum liklihood conditional classification algorithm
    def max_liklihood_conditional_classification(self):
        final_string = ""


        GivenData_Divided_By_Alldata = 0
        total_row_count = len(self.training_set.index)

        # get all unique categories in the category column
        category_col = self.category_column
        categories = self.training_set[category_col].unique()

        for category in categories:
            # Probability of the test data occurring given each category
            ProbData_Given_Category = self.ProbData_GivenCategory(category)

            category_df = self.create_subset(category)
            GivenData_Divided_By_Alldata += (ProbData_Given_Category * len(category_df.index))

        # GivenData_Divided_By_Alldata = ((ProbData_Given_Category * len(category_df.index)) + ...) / total_row_count
        GivenData_Divided_By_Alldata /= total_row_count

        # error catching
        if GivenData_Divided_By_Alldata == 0:
            print("Insufficient data to estimate the test sets' categories, quitting program")
            sys.exit(0)

        for category in categories:
            category_df = self.create_subset(category)
            category_df_length = len(category_df.index)

            # Probability of each category occuring in the training set--in general--not based off the test set
            Prob_GivenCategory = category_df_length / total_row_count

            # Probability of each category occuring given the test data
            Final_Probability = self.ProbCategory_GivenData(Prob_GivenCategory, GivenData_Divided_By_Alldata, category)
            print(f"{category}: {Final_Probability * 100:.2f}%")
            final_string += f"{category}: {Final_Probability * 100:.2f}%"

        return final_string
