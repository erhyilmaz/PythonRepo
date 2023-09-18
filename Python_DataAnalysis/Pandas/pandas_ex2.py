'''
LIST COMPREHENSIONS

TASK-2: List Comprehension yapısı kullanarak car_crashes verisinde isminde "no" barındırmayan
değişkenlerin isimlerinin sonuna "FLAG" yazınız.
'''

import numpy as np
import pandas as pd
import seaborn as sns

df = sns.load_dataset("car_crashes")
df.columns
df.head()


import numpy as np
import pandas as pd
import seaborn as sns
from pandas.api.types import is_numeric_dtype

pd.set_option('display.max_columns', 20)
df = sns.load_dataset("car_crashes")
df.columns
df.head()

[col.upper() + "_FLAG" if "no" not in col else col.upper() for col in df.columns]