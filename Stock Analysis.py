#!/usr/bin/env python
# coding: utf-8

# # Importing Libraries 

# In[5]:



import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import scipy.stats as st


# # Uploading Data Set

# In[6]:


df = pd.read_excel("/Users/josedhernandez/Desktop/Stocks_Feb_2020.xlsx")

# Printing the first & last 5 rows of the data set
df


# # Most & Least Profitable Trade

# In[16]:


# Most Profitable

df.loc[df['Profit Margin'].idxmax()]


# In[17]:


#Least Profitable

df.loc[df['Profit Margin'].idxmin()]


# # Plot Showing Trades

# In[21]:


#This shows that Amazon had the most & least profitable transaction

Cpalet = sns.palplot(sns.color_palette("husl", 8))
sns.catplot(x = "Name", y = "Profit Margin",hue = "Name",ci = None, color = Cpalet, data = df, aspect=1)


# # Total Profits for Month of February 
# 

# In[27]:


#Obtain total profits 
Profits = df.groupby('Name')['Profit Margin'].sum()
Profits


# In[25]:


df[["Profit Margin","Date of Sale"]].head()


# In[28]:


# Balance as in the account used to trade

Profits.sum() + 100000


# # Percentage Distribution

# In[50]:



labels = Profits.index
colors = colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#990077']
explode = (0.05,0.0,0.,0.4,0.0)

plt.title('Profit Percentage Distribution', fontsize = 15)

 


plt.pie(Profits,autopct='%1.1f%%',explode = explode,colors = colors, shadow = True);
plt.axis('equal')
plt.legend(labels, loc = "upper right") 
plt.tight_layout() 


# # Simple Linear Regression

# In[72]:


x = 'Purchased Price'
y = 'Selling Price'

sns.regplot(x,y, data = df, ci = None,fit_reg = True)


# # Statistics

# In[7]:


df.describe()


# In[ ]:




