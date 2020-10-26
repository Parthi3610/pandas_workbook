import pandas as pd
import numpy as np
from io import StringIO

fname = ["Paul","John","Richard","George"]
lname = ["McCartney", "Lennon", "Starkey", "Harrison"]
birth = [1942, 1940, 1940, 1943]

people = {"first":fname, "last":lname, "birth":birth}

beatles = pd.DataFrame(people, index = ['a', 'b', 'c', 'd'])
print(beatles)

fout = StringIO()
beatles.to_csv(fout)

print(fout.getvalue())

_ = fout.seek(0)
print(pd.read_csv(fout, index_col = 0))

diamonds = pd.read_csv("../data/diamonds.csv", nrows = 1000,
                       dtype ={
                           "carat": np.float32,
                           "depth": np.float32,
                           "table": np.float32,
                           "price": np.int16,
                           "x": np.float32,
                           "y": np.float32,
                           "z": np.float32
                       },
                       )
print(diamonds.info())

print(diamonds.describe())

print(diamonds.cut.value_counts())
print(diamonds.color.value_counts())
print(diamonds.clarity.value_counts())



