#merge both files
import pandas as pd   
import numpy as np 

EMPLOYEE_TABLE = pd.read_csv(r"C:\Users\marwan\Desktop\Employee.csv")

PF_TABLE= pd.read_csv(r"C:\Users\marwan\Desktop\performance table.csv")



merged_df = EMPLOYEE_TABLE.merge(PF_TABLE, left_on='EmployeeID', right_on='EmployeeID', how='inner')
merged_df['HireDate'] = pd.to_datetime(merged_df['HireDate'])
merged_df['ReviewDate'] = pd.to_datetime(merged_df['ReviewDate'])
merged_df.info()
merged_df.to_csv("E&PF_FINAL.csv", index=False)  