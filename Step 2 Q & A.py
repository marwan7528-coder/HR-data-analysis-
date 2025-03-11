#!/usr/bin/env python
# coding: utf-8

# In[72]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns


# In[73]:


df = pd.read_csv("FinalProject.csv")


# In[74]:


df.head()


# In[75]:


##Number of unique employees
num_em = df["EmployeeID"].nunique()
print(f"Number unique employees : {num_em} ")


# In[92]:


## Age Distribution of Employees
plt.figure(figsize=(8,5))
sns.histplot(df['Age'], bins=20, kde=True)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of employees")
plt.show()


# In[77]:


##Number of employees by gender
gender_counts = df["Gender"].value_counts()
plt.figure(figsize=(6,6))
plt.pie(gender_counts,labels=gender_counts.index,autopct="%1.1f%%",colors=['blue','orange','green','red'])
plt.title("Ratio Of Employees By Gender")
plt.show()


# In[78]:


##Distribution of employees by departments
plt.figure(figsize=(8,5))
sns.countplot(y =df['Department'],order=df['Department'].value_counts().index)
plt.title("Distribution of Employees By Departments")
plt.xlabel("Count_Employees")
plt.ylabel("Departments")
plt.show()


# In[79]:


##Distribution of employees by EducationLevel
plt.figure(figsize=(8,5))
sns.countplot(y =df['EducationLevel'],order=df['EducationLevel'].value_counts().index)
plt.title("Distribution of EducationLevel By Departments")
plt.xlabel("Count_Employees")
plt.ylabel("EducationLevel")
plt.show()


# In[80]:


##Salary Statistics
df['Salary'].describe()


# In[81]:


##Average Salary by Department
plt.figure(figsize=(10, 5))
sns.barplot(x=df.groupby('Department')['Salary'].mean().index, y=df.groupby('Department')['Salary'].mean().values)
plt.title("Average Salary by Department")
plt.xticks(rotation=45)
plt.ylabel("Average Salary")
plt.show()


# In[82]:


##The effect of education level on average salary
plt.figure(figsize=(10, 5))
sns.barplot(x=df.groupby('EducationLevel')['Salary'].mean().index, y=df.groupby('EducationLevel')['Salary'].mean().values)
plt.title("Average Salary by EducationLevel")
plt.xlabel("EducationLevel")
plt.ylabel("Average Salary")
plt.show()


# In[83]:


###The relationship between training opportunities and the number of courses
plt.figure(figsize=(8,5))
sns.lineplot(x =df['TrainingOpportunitiesWithinYear'],y=df['TrainingOpportunitiesWithinYear'])
plt.title("Training Opportunities vs. Number of Courses Taken")
plt.xlabel("Training Opportunities")
plt.ylabel("Courses Taken")
plt.show()


# In[84]:


attrition_rate = df['Attrition'].mean() * 100
print(f"Attrition_Rate : {attrition_rate:.2f}%")


# In[86]:


##the relationship Age vs. Attrition
plt.figure(figsize=(8, 5))
sns.boxplot(x=df['Attrition'], y=df['Age'])
plt.title("Age vs. Attrition")
plt.xlabel("Attrition")
plt.ylabel("Age")
plt.show()


# In[88]:


# Effect of distance from home on departure rate
plt.figure(figsize=(8, 5))
sns.boxplot(x=df['Attrition'], y=df['DistanceFromHome_KM'])
plt.title("Distance from Home vs. Departure")
plt.xlabel("Departure")
plt.ylabel("Distance from Home (km)")
plt.show()


# In[89]:


##The effect of overtime on leaving
plt.figure(figsize=(6, 4))
sns.countplot(x=df['OverTime'], hue=df['Attrition'])
plt.title("Effect of Overtime on Leave")
plt.xlabel("Overtime")
plt.ylabel("Number of Employees")
plt.show()


# In[91]:


##Analysis of years of work in the company
plt.figure(figsize=(8, 5))
sns.histplot(df['YearsAtCompany'], bins=20, kde=True)
plt.title("Years at Company")
plt.xlabel("Years")
plt.ylabel("Employees")
plt.show()


# In[94]:


##Analyze years of experience with the manager and its impact on performance
plt.figure(figsize=(12, 6))
sns.boxplot(x=df['manager_rating'], y=df['YearsWithCurrManager'])
plt.title("Years with Manager vs. Performance Rating")
plt.xlabel("Manager Rating")
plt.ylabel("Years with Manager")
plt.show()


# In[ ]:





# In[ ]:




