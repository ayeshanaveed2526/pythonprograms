
import pandas as pd
import numpy as np

def create_dummy_data():
    # Dummy data for Class A
    classA_data = {
        'Student_ID': ['S001', 'S002', 'S003', 'S004', 'S005'],
        'Name': ['Alice Johnson', 'Bob Smith', 'Charlie Brown', 'Diana Prince', 'Ethan Hunt'],
        'Age': [20, 21, 19, 22, 20],
        'Grade': ['A', 'B', 'A', 'C', 'B'],
        'Email': ['alice@email.com', 'bob@email.com', 'charlie@email.com', 'diana@email.com', 'ethan@email.com']
    }
    
    # Dummy data for Class B (with some overlapping students)
    classB_data = {
        'Student_ID': ['S003', 'S005', 'S006', 'S007', 'S008'],
        'Name': ['Charlie Brown', 'Ethan Hunt', 'Fiona Apple', 'George Lucas', 'Hannah Montana'],
        'Age': [19, 20, 21, 22, 20],
        'Grade': ['A', 'B+', 'A-', 'B', 'C+'],
        'Email': ['charlie@email.com', 'ethan@email.com', 'fiona@email.com', 'george@email.com', 'hannah@email.com']
    }
    
    # Create DataFrames
    df_classA = pd.DataFrame(classA_data)
    df_classB = pd.DataFrame(classB_data)
    
    # Save to Excel files
    df_classA.to_excel('students_classA.xlsx', index=False)
    df_classB.to_excel('students_classB.xlsx', index=False)
    
    print("Dummy files created successfully!")
    print("students_classA.xlsx created with 5 records")
    print("students_classB.xlsx created with 5 records")
    print("\nDuplicate Student_IDs: S003 and S005 (will be removed during merging)")

if __name__ == "__main__":
    create_dummy_data()
# ...existing code...
