import pandas as pd
import numpy as np

#college = pd.read_csv("C:/Users/preet/PycharmProjects/pandas_workbook/src/data/college.csv")
colleges = pd.read_csv("../data/college.csv", index_col="INSTNM")

colleges_val= colleges.filter(like="UGDS_")
print(colleges_val)

name = "Northwest-Shoals Community College"

print(colleges_val.loc[name])
print(colleges_val.loc[name].round(2))
print((colleges_val.loc[name]+.0001).round(2))

colleges_val_fin = (
    (colleges_val + 0.00501) // .01 / 100
)

print(colleges_val_fin.head())

print((colleges_val_fin+.000001).round(2))

print(colleges_val.add(0.00501).floordiv(.01).div(100))

print(colleges_val == 0.0333)

college_self_comp = colleges_val.fillna("") == colleges_val.fillna("")
print(college_self_comp.all())


print(colleges_val.isna().sum())
