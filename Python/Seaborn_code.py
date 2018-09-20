
# coding: utf-8

# In[1]:

#Set up
import os
os.chdir('C:\\Users\\amean\\Documents\\Coding\\Python')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import ExcelWriter
from pandas import ExcelFile

#import data
data = pd.read_excel('mock_attrition_data_4.xlsx', sheetname='Sheet1')
print("Column headings:")
print(data)

#seaborn
get_ipython().magic('matplotlib notebook')
import seaborn as sns
sns.set(style="darkgrid")

#Counts
sns.countplot(x='Grade', data=data)

# In[20]:

#linear regression model y~x (regplot)
sns.regplot(x='Service', y='Salary', data=data); 


# In[23]:

#linear regression model y~x (lmplot)
sns.lmplot(x='Service', y='Salary', data=data, x_jitter=.05)


# In[2]:

#logistic regression for binary variables
sns.lmplot(x='Salary', y='Attrition', data=data, logistic=True, y_jitter=.01)


# In[5]:

#use color to distinguish between 2 or more variables
sns.lmplot(x='Service', y='Salary', data=data, hue='Attrition', x_jitter=.05)


# In[19]:

#or use different markers
sns.lmplot(x='Service', y='Salary', hue='Attrition', data=data, markers=['o','x'], palette='Set1', ci=None)
#saving figs
plt.savefig('Salary vs Service Grid_2.png', dpi=300)


# In[16]:

#Draw multiple facets on rows or columns (col,row)
sns.lmplot(x='Service', y='Salary', hue='Attrition', data=data, col='Grade')

