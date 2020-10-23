import pandas as pd
import numpy as np

movies = pd.read_csv("C:/Users/preet/PycharmProjects/pandas_workbook/src/data/movie.csv")
movie_act_dir = movies[
    [
        "actor_1_name",
         "actor_2_name",
         "actor_3_name",
         "director_name"
    ]
]

print(movie_act_dir.head())

print(type(movies[["director_name"]]))
print(type(movies["director_name"]))


print(type(movies.loc[:,["director_name"]]))
print(type(movies.loc[:,"director_name"]))

def shorten(col):
    return (
        str(col).replace("facebook_likes","fb").replace("_for_reviews","")
    )
movies = movies.rename(columns = shorten)
print (movies.dtypes.value_counts())

print(movies.select_dtypes(include = "int64").head())

print(movies.select_dtypes(include = "float64").head())

print(movies.select_dtypes(include = "number").head())

print(movies.select_dtypes(include = ["int64","object"]).head())

print(movies.filter(like = 'fb').head())

print(movies.columns)

cat_core = [
    "movie_title",
    "title_year",
    "content_rating",
    "genres",
]
cat_people = [
    "director_name",
    "actor_1_name",
    "actor_2_name",
    "actor_3_name",
]
cat_other = [
    "color",
    "country",
    "language",
    "plot_keywords",
    "movie_imdb_link",
]
cont_fb = [
    "director_fb",
    "actor_1_fb",
    "actor_2_fb",
    "actor_3_fb",
    "cast_total_fb",
    "movie_fb",
]
cont_finance = ["budget", "gross"]
cont_num_reviews = [
    "num_voted_users",
    "num_user",
    "num_critic",
]
cont_other = [
    "imdb_score",
    "duration",
    "aspect_ratio",
    "facenumber_in_poster",
]

new_col_order = (cat_core+cat_people+cat_other+cont_fb+cont_finance+cont_num_reviews+cont_other)

print(set(movies.columns) == set(new_col_order))

print(movies[new_col_order].head())

print(movies.describe())

print(movies.describe().T)

print(movies.describe(percentiles=[0.01,0.3,1]).T)

print(movies.min(skipna=False))

print(movies.isnull().head())

print(movies.isnull().sum().head())

print(movies.isnull().sum().sum())

print(movies.select_dtypes(["object"]).fillna("").max())


