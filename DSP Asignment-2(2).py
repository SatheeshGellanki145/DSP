#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pandas as pd
df=pd.read_csv("Ecommerce purchases.csv")
df


# In[2]:


df.head()


# In[22]:


df.info()


# In[5]:


df["Purchase Price"].mean()


# In[23]:


df["Purchase Price"].max()


# In[7]:


df["Purchase Price"].min()


# In[8]:


df[df['Language']=='en'].count()


# In[9]:


df[df['Job']=='Lawyer'].info()


# In[10]:


df['AM or PM'].value_counts()


# In[19]:


df['Job'].value_counts().head(5)


# In[18]:


df[df['Lot']=='90 WT']['Purchase Price']


# In[16]:


df[df["Credit Card"]==4926535242672853]['Email']


# In[20]:


df[(df['CC Provider']=='Amarican Express')&(df['Purchase Price']>95)].count()


# In[ ]:





# In[ ]:




