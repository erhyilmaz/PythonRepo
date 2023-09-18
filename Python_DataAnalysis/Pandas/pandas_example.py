###############################
# Reading Data with Pandas
###############################
import numpy as np
import pandas as pd
import seaborn as sns


if 0:
    s = pd.Series([1, 3, 5, 7, 11])
    s.values
    s.ndim
    s.dtype
    s.size


    df = pd.read_csv("cities.csv")
    print(df.columns)
    print(df.head())
    print(df.tail())


pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

if 0:
    print(type(df[["age"]].head()))
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

    df.drop("age", axis=1).head()
    df.loc[:, ~df.columns.str.contains("age")].head()

    # iloc: integer based selection
    df.iloc[0:3]
    df.iloc[0, 0]
    df.iloc[0:3, 0:3]

    # loc: label based selection
    df.loc[0:3]
    df.loc[0:3, "age"]
    col_names = ["age", "embarked", "alive"]
    df.loc[0:3, col_names]

    # Conditional Selection
    df[df["age"] > 50].head()
    df[df["age"] > 50]["age"].count()

    df.loc[df["age"] > 50, "class"].head()
    df.loc[df["age"] > 50, ["age", "class"]].head()

    df["embark_town"].value_counts()

    df_new = df.loc[((df["age"] > 50)
                    & (df["sex"] == "male")
                    & ((df["embark_town"] == "Cherbourg") | (df["embark_town"] == "Southampton"))),
                    ["age", "class", "embark_town"]].head()

    df_new["embark_town"].value_counts()

    # Aggregation and Grouping
    # - count()
    # - first()
    # - last()
    # - mean()
    # - median()
    # - min()
    # - max()
    # - std()

    df["age"].mean()

    df.groupby("sex")["age"].mean()

    df.groupby("sex")["age"].mean()
    df.groupby("sex").agg({"age": ["mean", "sum"]})

    df.groupby("sex").agg({"age": ["mean", "sum"],
                           "survived": "mean"})

    df.groupby(["sex", "embark_town"]).agg({"age": ["mean"],
                           "survived": "mean"})

    df.groupby(["sex", "embark_town", "class"]).agg({"age": ["mean"],
                           "survived": "mean"})

    df.groupby(["sex", "embark_town", "class"]).agg({"age": ["mean"],
                           "survived": "mean",
                           "sex": "count"})

    # Pivot Tables
    df.pivot_table("survived", "sex", "embarked")

    df.pivot_table("survived", "sex", ["embarked", "class"])

    df.head()

    df["new_age"] = pd.cut(df["age"], [0, 10, 18, 25, 40, 90])
    df.pivot_table("survived", "sex", "new_age")


    # Apply and Lambda

    df["age2"] = df["age"]*2
    df["age3"] = df["age"]*5

    (df["age"]/10).head()
    (df["age2"]/10).head()
    (df["age3"]/10).head()

    for col in df.columns:
        if "age" in col:
            df[col] = df[col]/10
    df.head()

    # Lambda
    df[["age", "age2", "age3"]].apply(lambda x: x/10).head()
    df[["age", "age2", "age3"]].apply(lambda x: (x-x.mean())/x.std()).head()

    df.loc[:, df.columns.str.contains("age")].apply(lambda x: x/10).head()  # problem!!!
    df.loc[:, df.columns.str.contains("age")].apply(lambda x: (x-x.mean())/x.std()).head()  # problem!!!
    df.loc[:, df.columns.str.contains("age")] = df.loc[:, df.columns.str.contains("age")].apply(lambda x: (x-x.mean())/x.std()).head()  # problem!!!

# Join method

m = np.random.randint(1, 30, size=(5, 3))
df1 = pd.DataFrame(m, columns=["var1", "var2", "var3"])
df2 = df1 + 99

pd.concat([df1, df2])


df1 = pd.DataFrame({'employee': ['John', 'Dennis', 'Erhan', 'Mark', 'Maria'],
                    'group': ['account', 'HR', 'Engineer', 'doctor', 'teacher']})

df2 = pd.DataFrame({'employee': ['Erhan', 'John', 'Mark', 'Maria', 'Dennis'],
                    'start_date': [2010, 2001, 2012, 2014, 2000]})

df3 = pd.merge(df1, df2)  # ya da --> pd.merge(df1, df2, on="employee")

# Group manager info
df4 = pd.DataFrame({'group': ['account', 'HR', 'Engineer', 'doctor', 'teacher'],
                    'manager': ['Can', 'Deniz', 'Ali', 'Veli', 'Mustafa']})

df5 = pd.merge(df3, df4)  # ya da --> pd.merge(df3, df4, on="group")
df5.head()


