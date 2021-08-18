#!/usr/bin/env python
# coding: utf-8

# # 2021 Preppin' Data Challenge Week 1

# *Step 1: Importing Packages*

# In[51]:


import pandas as pd
import numpy as np
import datetime as dt
from matplotlib import pyplot as plt


# *Step 2: Importing Data*

# In[33]:


data= pd.read_csv('E:/Yash/Preppin Data Challenges/Week 1/PD 2021 Wk 1 Input - Bike Sales.csv')


# In[34]:


data.head()


# In[35]:


data.shape


# *Step 3: Preppin' Data*

# **Split the 'Store-Bike' field into 'Store' and 'Bike'**

# In[36]:


split_data= data['Store - Bike'].str.split("-",n=1,expand=True)


# In[37]:


final_data=data


# In[38]:


final_data['Store']=split_data[0]


# In[39]:


final_data['Bike']=split_data[1]


# In[40]:


final_data.drop(columns=["Store - Bike"],inplace=True)


# In[41]:


final_data.head()


# **Clean up the 'Bike' field to leave just three values in the 'Bike' field (Mountain, Gravel, Road)'**

# In[44]:


final_data['Bike']=final_data['Bike'].str.replace("Rood","Road")
final_data['Bike']=final_data['Bike'].str.replace("Rowd","Road")


# In[46]:


final_data['Bike']=final_data['Bike'].str.replace("Mountaen","Mountain")


# In[48]:


final_data['Bike']=final_data['Bike'].str.replace("Graval","Gravel")
final_data['Bike']=final_data['Bike'].str.replace("Gravle","Gravel")


# In[56]:


final_data['Bike'].unique()


# **Create two different cuts of the date field: 'quarter' and 'day of month'**

# In[59]:


#Converting object type to date
final_data['Date']=pd.to_datetime(final_data['Date'])


# In[62]:


final_data['Date'].dtypes


# In[64]:


final_data['Quarter']=final_data['Date'].dt.quarter


# In[67]:


final_data['Day of Month']=final_data['Date'].dt.day


# In[79]:


final_data.head()


# In[ ]:


final_data.drop(columns=["Date"],inplace=True)


# **Remove the first 10 orders as they are test values**

# In[78]:


final_data=final_data[final_data['Order ID']>10].reset_index(drop=True)


# In[80]:


final_data.head()


# In[81]:


final_data.shape


# In[82]:


final_data.to_csv('Week1_CleanData.csv')


# In[84]:


print("Challenge Complete :)")

