#merging the small tables 
import pandas as pd 
import numpy as np


EDUCATION_LEVEL= pd.read_csv(r"C:\Users\marwan\Desktop\EducationLevel.csv", index_col=0)
print(EDUCATION_LEVEL.head())

primary_tables=pd.read_csv(r"C:\Users\marwan\Desktop\PRIMARY.csv", index_col=0)
primary_tables = primary_tables.rename(columns={'Education': 'EducationLevelID'})
primary_tables.to_csv('PRIMARY.csv', index=False)
primary_tables.info()

primary_tables = pd.merge(primary_tables,EDUCATION_LEVEL, on='EducationLevelID', how='right')
print(primary_tables)
primary_tables.info()
primary_tables.to_csv('PRIMARY.csv', index=False)




