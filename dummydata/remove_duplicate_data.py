
import pandas as pd
import os

def remove_duplicates_and_merge():
    # File paths - change these to your actual file names
    file1_path = 'students_classA.xlsx'
    file2_path = 'students_classB.xlsx'
    
    # Check if files exist
    if not os.path.exists(file1_path):
        print(f"Error: File '{file1_path}' not found!")
        return
    if not os.path.exists(file2_path):
        print(f"Error: File '{file2_path}' not found!")
        return
    
    try:
        # Read both Excel files
        print("Reading Excel files...")
        df1 = pd.read_excel(file1_path)
        df2 = pd.read_excel(file2_path)
        
        # Combine both dataframes
        combined_df = pd.concat([df1, df2], ignore_index=True)
        
        # Remove duplicates based on Student_ID
        cleaned_df = combined_df.drop_duplicates(subset=['Student_ID'], keep='first')
        
        # Save the cleaned data to a new Excel file
        output_filename = 'combined_students_cleaned.xlsx'
        cleaned_df.to_excel(output_filename, index=False)
        
        # Print summary
        print(f"\nSummary:")
        print(f"File 1 records: {len(df1)}")
        print(f"File 2 records: {len(df2)}")
        print(f"Combined records: {len(combined_df)}")
        print(f"Unique records: {len(cleaned_df)}")
        print(f"Duplicates removed: {len(combined_df) - len(cleaned_df)}")
        print(f"\nCleaned data saved to: {output_filename}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    remove_duplicates_and_merge()

