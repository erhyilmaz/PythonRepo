
import pandas as pd
import seaborn as sns
from pandas.api.types import is_numeric_dtype

pd.set_option('display.max_columns', 20, 'display.width', 180)

new_exam_data = { 'Exam-1': {'Score': 0.0,
                             'Standing': 25,
                             'Questions': 90,
                             'Correct_Answers': 0,
                             'False_Answers': 0,
                             'No_Answers': 90,
                             'Tur': {'true': 0,
                                     'false': 0,
                                     'no_ans': 0
                                    },
                             'Mat': {'true': 0,
                                     'false': 0,
                                     'no_ans': 0
                                    },
                             'Fen': {'true': 0,
                                     'false': 0,
                                     'no_ans': 0
                                    },
                             'Sos': {'true': 0,
                                     'false': 0,
                                     'no_ans': 0
                                    },
                             'Din': {'true': 0,
                                     'false': 0,
                                     'no_ans': 0
                                    },
                             'Ing': {'true': 0,
                                     'false': 0,
                                     'no_ans': 0
                                    },
                             },
                  'Exam-2': {'Score': 0.0,
                             'Standing': 25,
                             'Questions': 90,
                             'Correct_Answers': 0,
                             'False_Answers': 0,
                             'No_Answers': 90,
                             'Tur': {'true': 0,
                                     'false': 0,
                                     'no_ans': 0
                                    },
                             'Mat': {'true': 0,
                                     'false': 0,
                                     'no_ans': 0
                                    },
                             'Fen': {'true': 0,
                                     'false': 0,
                                     'no_ans': 0
                                    },
                             'Sos': {'true': 0,
                                     'false': 0,
                                     'no_ans': 0
                                    },
                             'Din': {'true': 0,
                                     'false': 0,
                                     'no_ans': 0
                                    },
                             'Ing': {'true': 0,
                                     'false': 0,
                                     'no_ans': 0
                                    },
                             },
                }

columns = ('Score', 'Standing', 'Questions', 'Correct_Answers', 'False_Answers', 'No_Answers', 'Tur', 'Mat', 'Fen', 'Sos', 'Din', 'Ing')

#df = pd.DataFrame(data=data).T  # transpose
df = pd.DataFrame(data=new_exam_data, index=columns)  # order of keys in dict is guaranteed

print(df.columns)
print(df.head())

df.to_csv('exam_data.csv',index=True)
# df.to_csv('data.csv',  index=False) # columns are not written

df2 = pd.read_csv('data.csv', index_col=False)

# New entry to append
df_new = pd.DataFrame(data=new_exam_data, index=columns)  # order of keys in dict is guaranteed
# Display the updated DataFrame
print(df_new)

print("----------------------------------------------------------------------------------------------------------")

# Append the new entry using loc
df = pd.concat([df, df_new], axis=0, ignore_index=False)

df.to_csv('exam_data.csv')

# Display the updated DataFrame
print(df)


