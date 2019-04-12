import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import tree
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


pd.set_option('mode.chained_assignment', None)
pd.set_option('display.float_format', '{:,.2f}'.format)

data = pd.read_csv("https://github.com/autumntoney/predict_the_box_office/raw/master/movie_metadata.csv")


#  ----------- Data Cleaning Phase ----------


#  printing the number of duplicates in the data
print('Number of duplicates in : {}'.format(
    sum(data.duplicated(subset=['movie_title', 'title_year'], keep=False))),"\n")

# Fixing null & zero values, dropping duplicates
data = data.drop_duplicates(subset=['move_title', 'title_year'], keep='first').copy()
data.isnull().values.any()
data = data.drop_duplicates(subset=['movie_title', 'title_year'], keep='first').copy()


#  function to check how many values are null within each column
def show_missing_data(data):
    missing_data = data.isnull().sum().reset_index()
    missing_data.columns = ['column_name', 'missing_count']
    missing_data['filling_factor'] = (data.shape[0] - missing_data['missing_count']) / data.shape[0] * 100
    return missing_data.sort_values('filling_factor').reset_index(drop=True)


print('Missing data:\n', show_missing_data(data)[:5])

#  Going to drop rows which don't have 'gross' in them, since it's a vital attribute
data.dropna(subset=['gross'], how='all', inplace=True)
print(show_missing_data(data)[:5])

median_budget_per_year = data.groupby('title_year')['budget'].transform('median')
data['budget'].fillna(median_budget_per_year, inplace=True)

print(show_missing_data(data)[:5])

data.fillna(0, inplace=True)  # Fill rest of missing data
data = data[data['title_year'] != 0]  # Deleting rows where title_year = 0
data = data[data['country'] == 'USA']  # Budgets are in respective country currency, so we will drop it


#  ----------- Data Cleaning Phase ----------
