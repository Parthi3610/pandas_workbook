import pandas as pd
import numpy as np

movies = pd.read_csv("C:/Users/Preethi/PycharmProjects/pandas_workbook/src/data/movie.csv")
index = movies.index
columns = movies.columns
data = movies.to_numpy()

print("index is:", index)
print("columns is:", columns)
print("data is:", data)

print(type(index))
print(type(columns))
print(type(data))

print(index.to_numpy())
print(columns.to_numpy())

print(movies.dtypes)
print(movies.dtypes.value_counts())
print(movies.info())
print(movies["director_name"])
print(movies.duration)
