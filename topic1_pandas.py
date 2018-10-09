
# coding: utf-8

# In[68]:


import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('https://raw.githubusercontent.com/Yorko/mlcourse.ai/master/data/adult.data.csv')


# In[22]:


df


# In[41]:


(df['native-country'].value_counts(normalize=True)*100).Germany


# In[42]:


df[df['sex']=='Female']['age'].mean()


# In[33]:


print(df[df['salary']=='>50K']['age'].mean())
print(df[df['salary']=='>50K']['age'].std())


# In[35]:


print(df[df['salary']=='<=50K']['age'].mean())
print(df[df['salary']=='<=50K']['age'].std())


# In[40]:


print(df[df['salary']=='>50K']['education'].unique())


# In[46]:


print(max(df[df['race']=='Amer-Indian-Eskimo']['age']))


# In[ ]:


print(max(df[df['marital-status']=='Amer-Indian-Eskimo']['age']))


# In[47]:


df['marital-status'].unique()


# In[52]:


df[(df['sex']=='Male') & (df['salary']=='>50K')]['marital-status']


# In[64]:


marriedDF=df[df['salary']=='>50K']
married=(['Married-civ-spouse','Married-spouse-absent','Married-AF-spouse'])
marriedDF['married?']=marriedDF['marital-status'].replace(married,True)
marriedDF["married?"].loc[~(marriedDF["married?"]==True)]=False
marriedDF["married?"].value_counts()


# In[76]:


marriedDF=df
married=(['Married-civ-spouse','Married-spouse-absent','Married-AF-spouse'])
marriedDF['married?']=marriedDF['marital-status'].replace(married,True)
marriedDF["married?"].loc[~(marriedDF["married?"]==True)]=False
plt.figure()
print(pd.crosstab(df['married?'], df['salary']))
pd.crosstab(df['married?'], df['salary']).plot.bar()
plt.show()


# In[78]:


print(max(df['hours-per-week']))
print(df[df['hours-per-week']==max(df['hours-per-week'])]['salary'].value_counts(normalize=True)*100)


# In[95]:


print(df[(df['native-country']=='Japan') & (df['salary']=='>50K')]['hours-per-week'].mean())
print(df[(df['native-country']=='Japan') & (df['salary']=='<=50K')]['hours-per-week'].mean())


# In[83]:


df[df['native-country']=='Japan']['hours-per-week'].mean()

