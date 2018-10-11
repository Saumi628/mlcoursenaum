
# coding: utf-8

# In[6]:


import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("E:/ML/120-years-of-olympic-history-athletes-and-results/athlete_events.csv")


# In[37]:


df


# In[12]:


print(min(df[(df['Year']==1996)&(df['Sex']=='M')]['Age']))
print(min(df[(df['Year']==1996)&(df['Sex']=='F')]['Age']))


# In[23]:


len(df[(df['Sport']=='Gymnastics') & (df['Sex']=='M')&(df['Year']==2000)])/len(df[(df['Sex']=='M')&(df['Year']==2000)])*100


# In[26]:


print(df[(df['Year']==2000)&(df['Sex']=='F')&(df['Sport']=='Basketball')]['Height'].mean())
print(df[(df['Year']==2000)&(df['Sex']=='F')&(df['Sport']=='Basketball')]['Height'].std())


# In[30]:


maxWeight=max(df[(df['Year']==2002)]['Weight'])
print(maxWeight)
print(df[(df['Year']==2002)&(df['Weight']==maxWeight)]['Sport'])


# In[35]:


len(df[(df['Name']=='Pawe Abratkiewicz')]['Year'].unique())


# In[34]:


df[(df['Team']=='Australia')]


# In[51]:


df[(df['Year']==2000)&(df['Team']=='Australia')].groupby(['Team','Sport','Medal'])['Medal'].count()


# In[63]:


df2016=df[df['Year']==2016]
pd.crosstab(df2016[df2016['Team'].isin(['Serbia','Switzerland'])]['Team'],df2016['Medal'], margins=True)


# In[85]:


labels = ["[{0}-{1})".format(i, i + 10) for i in range(5, 105, 10)]
df['group'] = pd.cut(df.Age, range(5, 115, 10), right=False, labels=labels)
df[df['Year']==2014]['group'].value_counts()


# In[90]:


df[df['City'].isin(['Lake Placid','Sankt Moritz'])].groupby(['Season','City','Year'])[['Season','City']].count()


# In[97]:


print(len(df[df['Year']=2016]['Sport'].unique()))
print(len(df[df['Year']=1995]['Sport'].unique()))
print(len(df[df['Year']=2016]['Sport'].unique())-len(df[df['Year']=1995 ]['Sport'].unique()))


# In[73]:


df[~(df['Sport']=='Art Competitions')].sort_values(['Age'],ascending=False)

