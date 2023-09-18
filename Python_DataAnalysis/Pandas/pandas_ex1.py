'''
LIST COMPREHENSIONS

TASK-1: List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük
harfe çeviriniz ve başına NUM ekleyiniz.

Tip: Numeric olmayan değişkenlerin de isimleri büyümeli. Tek bir list comprehension yapısı kullanılmalı.
'''

import numpy as np
import pandas as pd
import seaborn as sns
from pandas.api.types import is_numeric_dtype

pd.set_option('display.max_columns', 20)
df = sns.load_dataset("car_crashes")
df.columns
df.head()

["NUM_" + col.upper() if is_numeric_dtype(df[col].dtype) else col.upper() for col in df.columns]

