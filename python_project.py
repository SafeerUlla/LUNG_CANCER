#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_csv("c:\\users\\safee\\oneDrive\\Desktop\\me.csv")


# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


import seaborn as sns
df=pd.read_csv("c:\\users\\safee\\oneDrive\\Desktop\\me.csv")
ax=sns.lineplot(x='AGE',y='GENDER',data=df)


# In[6]:


import seaborn as sns
df=pd.read_csv("c:\\users\\safee\\oneDrive\\Desktop\\me.csv")
ax=sns.lineplot(x='AGE',y='GENDER',data=df,hue='LUNG_CANCER')


# In[7]:


import seaborn as sns
df=pd.read_csv("c:\\users\\safee\\oneDrive\\Desktop\\me.csv")
ax=sns.heatmap(df.corr())


# In[9]:


import seaborn as sns
df=pd.read_csv("c:\\users\\safee\\oneDrive\\Desktop\\me.csv")
ax=sns.heatmap(df.corr(),cmap='RdBu')


# In[10]:


import seaborn as sns
df=pd.read_csv("c:\\users\\safee\\oneDrive\\Desktop\\me.csv")
ax=sns.heatmap(df.corr(),cmap='RdBu',annot=True);


# In[11]:


import seaborn as sns
df=pd.read_csv("c:\\users\\safee\\oneDrive\\Desktop\\me.csv")
ax=sns.heatmap(df.corr(),cmap='RdBu',linewidth=1);


# In[12]:


import seaborn as sns
df=pd.read_csv("c:\\users\\safee\\oneDrive\\Desktop\\me.csv")
ax=sns.pairplot(df,hue="AGE",size=3);


# In[13]:


import seaborn as sns
df=pd.read_csv("c:\\users\\safee\\oneDrive\\Desktop\\me.csv")
ax=sns.histplot(df,log_scale=True)


# In[14]:


import seaborn as sns
df=pd.read_csv("c:\\users\\safee\\oneDrive\\Desktop\\meo.csv")
ax=sns.histplot(df,log_scale=True)


# In[15]:


import seaborn as sns
df=pd.read_csv("c:\\users\\safee\\oneDrive\\Desktop\\meo.csv")
ax=sns.pairplot(df,hue="AGE",size=3);


# In[ ]:




