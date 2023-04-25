import pandas as pd
import Climbing_Grade_Proj_Functions as Functions
import matplotlib.pyplot as plt
import seaborn as sns




if __name__ == "__main__":
    df = Functions.get_data()
    sns.displot(df, x="Jugs")
    plt.show()
