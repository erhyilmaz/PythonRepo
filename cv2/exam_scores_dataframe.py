
from IPython.display import display, HTML
import matplotlib.pyplot as plt
import os
#from os import path
import os.path as path
import pandas as pd
import seaborn as sns
from pandas.api.types import is_numeric_dtype

pd.set_option('display.max_columns', 20, 'display.width', 220)

columns = ('Exam', 'Score', 'Standing', 'Tot_Q',
           'Tot_CorrAns', 'Tot_FalseAns', 'Tot_NoAns',
           'Tur_T', 'Tur_F', 'Tur_NA',
           'Mat_T', 'Mat_F', 'Mat_NA',
           'Fen_T', 'Fen_F', 'Fen_NA',
           'Sos_T', 'Sos_F', 'Sos_NA',
           'Din_T', 'Din_F', 'Din_NA',
           'Ing_T', 'Ing_F', 'Ing_NA')

new_exam_data = { 'Exam': [3],
                  'Score': [15.0],
                  'Standing': [21],
                  'Tot_Q': [90],
                  'Tot_CorrAns': [0], 'Tot_FalseAns': [0], 'Tot_NoAns': [0],
                  'Tur_T': [0], 'Tur_F': [0], 'Tur_NA': [0],
                  'Mat_T': [0], 'Mat_F': [0], 'Mat_NA': [0],
                  'Fen_T': [0], 'Fen_F': [0], 'Fen_NA': [0],
                  'Sos_T': [0], 'Sos_F': [0], 'Sos_NA': [0],
                  'Din_T': [0], 'Din_F': [0], 'Din_NA': [0],
                  'Ing_T': [0], 'Ing_F': [0], 'Ing_NA': [0],
                }

# df_new = pd.DataFrame(data=data).T  # transpose
# df_new = pd.DataFrame(data=new_exam_data, index=columns)  # order of keys in dict is guaranteed
df_new = pd.DataFrame(data=new_exam_data)

# ---- Display the updated DataFrame
# print(df_new.columns)
# print(df_new.head())
# print(df_new)

file_name = 'exam_data.csv'
file_path = os.path.isfile(file_name)
if file_path:
    print('File exists!')

    # Read csv data
    df = pd.read_csv(file_name, index_col=[0])

    # ------- Append the new entry using loc
    df = pd.concat([df, df_new], ignore_index=True)
    # df = pd.concat([df, df_new], axis=0, ignore_index=True)
    # df = df.append(df_new, ignore_index=True)
    # print(df)

    # ------ Write new concatenated data frame into csv file
    df.to_csv(file_name, index=True)

else:
    print('File does NOT exist!')
    fp = open(file_name, 'x')
    fp.close()

    # Write initial data frame into csv file
    df_new.to_csv(file_name, index=True)

# Display saved entries
df_read = pd.read_csv(file_name, index_col=[0])
print('Display---------------')
print(df_read)


# ---------- Displaying Scores ------------------

#df_read.plot(y='Score', figsize=(10,6))


print('Plot---------------')
# Plotting a scatter plot
#df.plot(x='Exam', y='Score', kind='scatter', color='green', marker='D')
df.plot(x='Exam', y='Score', kind='bar', color='green')
plt.title('Scatter Plot Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

if 0:
    # Usage of size(), unstack()
    class_scores = df_read.groupby(['Exam', 'Score'])
    print(class_scores)
    # size() - to count number of rows in each grouping
    print(class_scores.size())
    # unstack() - to convert results into a more readable format.
    print(class_scores.size().unstack())

    # Visualization of scores per exam
    class_scores.size().unstack().plot(kind='bar', stacked=True, colormap='autumn')
    plt.xlabel('Exam name')
    plt.ylabel('-----------')
    plt.title('++++++++++++')
    plt.show()

    # Visualization of scores per exam
    class_scores.size().plot(kind='bar', stacked=True, colormap='autumn')
    plt.xlabel('Exam name')
    plt.ylabel('-----------')
    plt.title('++++++++++++')
    plt.show()