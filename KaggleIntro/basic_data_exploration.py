# On the use of the Pandas library for data exploration

import pandas as pd

melbourne_path = "../input/melbourne-housing-snapshot/melb_data.csv"
# Read the data and store as a pandas dataframe
melbourne_data = pd.read_csv(melbourne_path)
# print a summary of the data
melbourne_data.describe()

