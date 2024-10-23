"""
Name:  Ashleigh Wong
Email:  ashleigh.wong12@myhunter.cuny.edu
Resources: Used python.org as a reminder of Python 3 print statements.
"""
import pandas as pd
input_file = input("Enter input file name: ")
output_file = input("Enter output file name: ")
df = pd.read_csv(input_file)
df_filtered = df[df['senate_class'].notna() & (df['senate_class'] != '')]
df_out = df_filtered[['first_name', 'last_name']]
df_out.to_csv(output_file, index=False)
#End-of-file (EOF)
