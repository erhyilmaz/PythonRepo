###############################
# Reading Data with Pandas
###############################

import pandas as pd
import seaborn as sns


#df = pd.read_csv("cities.csv")
#print(df.columns)
#print(df.head())
#print(df.tail())


df = sns.load_dataset("titanic")
df.head()
df.tail()
df.shape
df.info()
df.columns
df.index
df.describe().T
df.isnull().values.any()
df.isnull().sum()
df["sex"].head()
df["sex"].value_counts()

