# Import pandas library
import pandas as pd

# Import the data
nasdaq = pd.read_csv('nasdaq-listings.csv')

# Display first 10 rows
print(nasdaq.head(10))

# Inspect nasdaq
nasdaq.info()


# Import the data
nasdaq = pd.read_csv('nasdaq-listings.csv', na_values='NAN', parse_dates=['Last Update'])

# Display the head of the data
print(nasdaq.head())

# Inspect the data
nasdaq.info()

# Import the data
nyse = pd.read_excel('listings.xlsx', sheetname='nyse',na_values='n/a')

# Display the head of the data
print(nyse.head())

# Inspect the data
nyse.info()


