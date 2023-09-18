'''
LIST COMPREHENSIONS

TASK-3: List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan
değişkenlerin isimlerini seçiniz ve yeni bir dataframe oluşturunuz.

og_list = ["abbrev", "no_previous"]

Tip: Önce verilen listeye göre list comprehension kullanarak new_cols adında yeni liste oluşturunuz.
Sonra df[new_cols] ile bu değişkenleri seçerek yeni bir df oluşturunuz ve adını new_df olarak isimlendiriniz.

'''

import numpy as np
import pandas as pd
import seaborn as sns

df = sns.load_dataset("car_crashes")
df.columns
df.head()

og_list = ["abbrev", "no_previous"]

new_col = [col for col in df.columns if col not in og_list]
df2 = df[new_col]