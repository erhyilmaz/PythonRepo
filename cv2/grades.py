import csv
import pandas as pd

def save_dict_to_csv(filename, data_dict):
    with open(filename, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        # Write the header with column names
        writer.writerow(data_dict.keys())
        # Write the data
        writer.writerow(data_dict.values())

def append_to_csv(filename, data_dict):
    with open(filename, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(data_dict.keys())  # Write the header
        writer.writerows(data_dict.values())  # Write the data

def load_dict_from_csv(filename):
    data_dict = {}
    with open(filename, 'r') as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)
        for col in header:
            data_dict[col] = []
        for row in reader:
            for col, value in zip(header, row):
                data_dict[col].append(value)
    return data_dict


# Example data (a dictionary)
if 0:
    data_dict = {
        'Name': ['Ex-1', 'Ex-2', 'Ex-3'],
        'Score': [425, 330, 422],
        'Standing': [25, 12, 8],
        'Total_Ques': [90, 90, 90],
        'Tur': {'true': [1, 2, 3],
                'false': [1, 2, 3],
                'no_ans': [1, 2, 3],
               },
        'Mat': {'true': [1, 2, 3],
                'false': [1, 2, 3],
                'no_ans': [1, 2, 3],
               },
        'Fen': {'true': [1, 2, 3],
                'false': [1, 2, 3],
                'no_ans': [1, 2, 3],
               },
        'Sos': {'true': [1, 2, 3],
                'false': [1, 2, 3],
                'no_ans': [1, 2, 3],
               },
        'Din': {'true': [1, 2, 3],
                'false': [1, 2, 3],
                'no_ans': [1, 2, 3],
               },
        'Ing': {'true': [1, 2, 3],
                'false': [1, 2, 3],
                'no_ans': [1, 2, 3],
               },
    }

data_dict = {'Exam_Name': 'Exam-1',
             'Score': 0.0,
             'Standing': 25,
             'Tot_Q': 90,
             'Tot_CorrAns': 0, 'Tot_FalseAns': 0, 'Tot_NoAns': 0,
             'Tur_T': 0, 'Tur_F': 0, 'Tur_NA': 0,
             'Mat_T': 0, 'Mat_F': 0, 'Mat_NA': 0,
             'Fen_T': 0, 'Fen_F': 0, 'Fen_NA': 0,
             'Sos_T': 0, 'Sos_F': 0, 'Sos_NA': 0,
             'Din_T': 0, 'Din_F': 0, 'Din_NA': 0,
             'Ing_T': 0, 'Ing_F': 0, 'Ing_NA': 0,
 }

# Save the dictionary to a CSV file
save_dict_to_csv('data.csv', data_dict)

# Load the CSV file
loaded_data = load_dict_from_csv('data.csv')

# Append a new entry to the loaded data
new_entry = {'Exam_Name': 'Exam-2',
             'Score': 0.0,
             'Standing': 25,
             'Tot_Q': 90,
             'Tot_CorrAns': 0, 'Tot_FalseAns': 0, 'Tot_NoAns': 0,
             'Tur_T': 0, 'Tur_F': 0, 'Tur_NA': 0,
             'Mat_T': 0, 'Mat_F': 0, 'Mat_NA': 0,
             'Fen_T': 0, 'Fen_F': 0, 'Fen_NA': 0,
             'Sos_T': 0, 'Sos_F': 0, 'Sos_NA': 0,
             'Din_T': 0, 'Din_F': 0, 'Din_NA': 0,
             'Ing_T': 0, 'Ing_F': 0, 'Ing_NA': 0,
 }

loaded_data['Exam_Name'].append(new_entry['Exam_Name'])
loaded_data['Score'].append(new_entry['Score'])
loaded_data['Standing'].append(new_entry['Standing'])
loaded_data['Tot_Q'].append(new_entry['Tot_Q'])
loaded_data['Tot_CorrAns'].append(new_entry['Tot_CorrAns'])
loaded_data['Tot_FalseAns'].append(new_entry['Tot_FalseAns'])
loaded_data['Tot_NoAns'].append(new_entry['Tot_NoAns'])
loaded_data['Tur_T'].append(new_entry['Tur_T'])
loaded_data['Tur_F'].append(new_entry['Tur_F'])
loaded_data['Tur_NA'].append(new_entry['Tur_NA'])
loaded_data['Mat_T'].append(new_entry['Mat_T'])
loaded_data['Mat_F'].append(new_entry['Mat_F'])
loaded_data['Mat_NA'].append(new_entry['Mat_NA'])
loaded_data['Fen_T'].append(new_entry['Fen_T'])
loaded_data['Fen_F'].append(new_entry['Fen_F'])
loaded_data['Fen_NA'].append(new_entry['Fen_NA'])
loaded_data['Sos_T'].append(new_entry['Sos_T'])
loaded_data['Sos_F'].append(new_entry['Sos_F'])
loaded_data['Sos_NA'].append(new_entry['Sos_NA'])
loaded_data['Din_T'].append(new_entry['Din_T'])
loaded_data['Din_F'].append(new_entry['Din_F'])
loaded_data['Din_NA'].append(new_entry['Din_NA'])
loaded_data['Ing_T'].append(new_entry['Ing_T'])
loaded_data['Ing_F'].append(new_entry['Ing_F'])
loaded_data['Ing_NA'].append(new_entry['Ing_NA'])

# Append the new entry to the CSV file
append_to_csv('data.csv', loaded_data)


# Display the dictionary contents
for key, values in loaded_data.items():
    print(f"{key}: {values}")

# If you want to display the data in a more tabular format:
print("\nTabular Format:")
for i in range(len(loaded_data['Name'])):
    for key, values in loaded_data.items():
        print(f"{key}: {values[i]}\t", end="")
    print()  # Move to the next line for the next entry

# Create a DataFrame from the dictionary
df = pd.DataFrame(loaded_data)

# Display the DataFrame
print(df)


#------------------------------------------------------------------------------
if 0 :
    # Initialize an empty dictionary to hold exam data
    exam_data = {}

    # Function to add exam data
    def add_exam(student_id, course, exam_name, exam_data_dict):
        if student_id not in exam_data:
            exam_data[student_id] = {}
        if course not in exam_data[student_id]:
            exam_data[student_id][course] = {}
        exam_data[student_id][course][exam_name] = exam_data_dict

    # Function to display exam data for a specific student, course, and exam
    def display_exam_data(student_id, course, exam_name):
        if student_id in exam_data and course in exam_data[student_id] and exam_name in exam_data[student_id][course]:
            print(f"Exam data for Student {student_id} in {course} - {exam_name}:")
            exam_data_dict = exam_data[student_id][course][exam_name]
            for question, options in exam_data_dict.items():
                print(f"Question {question}:")
                print(f"True: {options['true']}, False: {options['false']}, Unanswered: {options['unanswered']}")
        else:
            print(f"No exam data available for Student {student_id} in {course} - {exam_name}.")

    # Example usage:
    exam_data_dict = {
        'student_name': 'Ahmet Kerem',
        'exam-name': 'Exam-1',
        'score': 400.0,
        'standing': 25,
        'total_participants': 60,
        'answers': {
            'TUR': {'total': 20, 'true': 1, 'false': 0, 'unanswered': 0},
            'MAT': {'total': 20, 'true': 1, 'false': 0, 'unanswered': 0},
            'FEN': {'total': 20, 'true': 1, 'false': 0, 'unanswered': 0},
            'SOS': {'total': 10, 'true': 1, 'false': 0, 'unanswered': 0},
            'DIN': {'total': 10, 'true': 1, 'false': 0, 'unanswered': 0},
            'ING': {'total': 10, 'true': 1, 'false': 0, 'unanswered': 0},
        }
    }

    add_exam("12345", "Math", "Midterm", exam_data_dict_1)

    display_exam_data("12345", "Math", "Midterm")
    display_exam_data("12345", "Science", "Final")
