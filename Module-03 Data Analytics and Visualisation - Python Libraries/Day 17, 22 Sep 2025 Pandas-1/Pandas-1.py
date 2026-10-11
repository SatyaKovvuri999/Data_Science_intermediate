# *****************************************************

# Pandas 1 | AGENDA
# =====================
#   - Intro to Pandas
#   - Dataframe & Series
#   - Operations of  Dataframe
#   - Operations on Columns
#   - Operations on rows
#   - loc & iloc

# ***********************************************************


# Intro to Pandas
# ===============
'''
Intro to Pandas
===============

* Why Pandas if we have Numpy?
    - Numpy can only be used for homogenous data
    - In case of tabular form of data Ex: csv


* Pandas is a fast powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language.
* Unlike numpyt Pandas can work with heterogenous data.



* Dataset we are working on https://drive.google.com/file/d/1E3bwvYGf1ig32RmcYiWc0IXPN-mD_bI_/view
'''




import pandas as pd

file_path = "Module-3 Data Analytics and Visualisation - Python Libraries\\Day 17, 22 Sep 2025 Pandas-1\\mckinsey.csv"

df = pd.read_csv(file_path)
print(df)
print(type(df))
# <class 'pandas.core.frame.DataFrame'>

# It is 2D matrix
# Each column is called series which is 1D matrix


print(type(df['country']))
# <class 'pandas.core.series.Series'>


# To get the information about the dataframe
print(df.info())
'''
RangeIndex: 1704 entries, 0 to 1703
Data columns (total 6 columns):
 #   Column      Non-Null Count  Dtype
---  ------      --------------  -----
 0   country     1704 non-null   object
 1   year        1704 non-null   int64
 2   population  1704 non-null   int64
 3   continent   1704 non-null   object
 4   life_exp    1704 non-null   float64        
 5   gdp_cap     1704 non-null   float64        
dtypes: float64(2), int64(2), object(2)
memory usage: 80.0+ KB
None
'''




print(df)



'''
Some basic operations on columns
================================
 - Add a column
  
'''


print(df.keys())


print(df.head())



print(df['country'])

# To fetch the first 5 values
print(df['country'].head())


# Accessing multiple columns

# To fetch the values of columns country and population
print(df[['country', 'population']])


# To fetch the values of columns country population and gdp_cap
print(df[['country', 'population','gdp_cap']])


# To fetch the unqiue values from the columns
print(df['country'].unique())

# To get the count of the unique values
print(len(df['country'].unique()))
# 142
print(len(df['country'].unique()))




