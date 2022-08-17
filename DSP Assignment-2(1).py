#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df=pd.read_csv("salaries.csv")
df


# In[2]:


df.head()


# In[3]:


df.tail()


# In[4]:


df.info()


# In[5]:


df["BasePay"].mean()


# In[6]:


df["OvertimePay"].max()


# In[7]:


df[df["EmployeeName"]=='JOSEPH DRISCOLL']


# In[9]:


df[df['EmployeeName']=='JOSEPH DRISCOLL']['TotalPayBenefits']


# In[10]:


df['TotalPayBenefits'].max()


# In[11]:


df[df['TotalPayBenefits']==df['TotalPayBenefits'].max()]


# In[14]:


df.loc[df['TotalPayBenefits'].idxmax()]


# In[15]:


df[df['TotalPayBenefits']==df['TotalPayBenefits'].min()]


# In[16]:


df.loc[df['TotalPayBenefits'].idxmin()]['EmployeeName']


# In[17]:


df.loc[df['TotalPayBenefits'].idxmin()]


# In[18]:


df.groupby('Year').mean()['BasePay']


# In[19]:


df['JobTitle'].value_counts().head(5)


# In[20]:


df[df['Year']==2013]['JobTitle'].value_counts()


# In[21]:


sum(df[df['Year']==2013]['JobTitle'].value_counts()==1)


# In[22]:


df['title_len']=df['JobTitle'].apply(len)


# In[23]:


df[['JobTitle','title_len']].head()


# In[24]:


df[['title_len','TotalPayBenefits']].corr()


# In[ ]:




