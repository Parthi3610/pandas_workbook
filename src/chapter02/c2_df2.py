import pandas as pd
import numpy as np

#college = pd.read_csv("C:/Users/preet/PycharmProjects/pandas_workbook/src/data/college.csv")
colleges = pd.read_csv("../data/college.csv", index_col="INSTNM")

colleges_ugds= colleges.filter(like="UGDS_")
print(colleges_ugds)

name = "Northwest-Shoals Community College"

print(colleges_ugds.loc[name])
print(colleges_ugds.loc[name].round(2))
print((colleges_ugds.loc[name]+.0001).round(2))

colleges_ugds_fin = (
    (colleges_ugds + 0.00501) // .01 / 100
)

print(colleges_ugds_fin.head())

print((colleges_ugds_fin+.000001).round(2))

print(colleges_ugds.add(0.00501).floordiv(.01).div(100))

print(colleges_ugds == 0.0333)

college_self_comp = colleges_ugds.fillna("") == colleges_ugds.fillna("")
print(college_self_comp.all())


print(colleges_ugds.isna().sum())


