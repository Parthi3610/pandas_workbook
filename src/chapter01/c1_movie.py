import pandas as pd
import numpy as np
import c1_debug1

movies = pd.read_csv("C:/Users/preet/PycharmProjects/pandas_workbook/src/data/movie.csv")
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
print(movies.loc[:,"director_name"])
print(movies.iloc[:,1])

print(movies["director_name"].index)
print(movies["director_name"].dtype)
print(movies["director_name"].size)
print(movies.director_name.name)

print(type(movies.director_name))
print(movies.director_name.apply(type).unique())

s_attr_methods = set(dir(pd.Series))
print(len(s_attr_methods))

df_attr_methods = set(dir(pd.DataFrame))
print(len(df_attr_methods))

print(len(s_attr_methods & df_attr_methods))

director = movies.director_name
print(director.dtype)


fb_likes = movies.actor_1_facebook_likes
print(fb_likes.dtype)

print(director.head())

print(director.sample(n=5,random_state = 42))

print(director.tail())

print(director.value_counts())
print(fb_likes.value_counts())

print(fb_likes.min())
print(fb_likes.max())
print(fb_likes.mean())
print(fb_likes.median())
print(fb_likes.std())

print(fb_likes.describe())
print(director.describe())

print(fb_likes.quantile([0.2, 1]))

print(director.isna())

print(fb_likes.count())
fb_likes_filled = fb_likes.fillna(0)
print(fb_likes_filled.count())

print(fb_likes.size)
fb_likes_dropped = fb_likes.dropna()
print(fb_likes_dropped.size)

print(director.value_counts(normalize = True))

imdb_score = movies.imdb_score
print(imdb_score)
print(imdb_score+1)

print(imdb_score.add(1))
print(imdb_score.gt(7))



money = pd.Series([100,20,None])
print(money - 15)

print(money.sub(15,fill_value = 0))

print(fb_likes.fillna(0).astype(int).head())


print(fb_likes.fillna(0).pipe(c1_debug1.debug_ser).astype(int).head())

interm = None

def get_interm(ser):
    global interm
    interm = ser
    return ser

fb_likes.fillna(0)\
    .pipe(get_interm)\
    .astype(int)\
    .head()
print(interm)

col_map = { "director_name":"director", "num_voted_users":"vote"}

print(movies.rename(columns=col_map).head(n=10))

index_map = { "Avatar":"Ratava", "Spectre":"Ertceps"}

print(movies.set_index("movie_title").rename(index=index_map,columns=col_map).head(3))

movies = pd.read_csv(("C:/Users/preet/PycharmProjects/pandas_workbook/src/data/movie.csv"),
         index_col = "movie_title")

idx = movies.index.to_list()
col = movies.columns.to_list()

idx[0] = 'Rat '
idx[1] = 'poc'
idx[2] = 'exc'
col[1] = 'director'
col[-1] = ' fb_ likes '
col[-2] = 'ar'

movies.index = idx
movies.columns = col
print(movies.head())


def to_cleanup(val):
    return val.strip().lower().replace(' ', '_')

print(movies.rename(columns=to_cleanup).head())

cols = [
    col.strip
    for col in movies.columns
]

movies.columns = cols
print(movies.head())

