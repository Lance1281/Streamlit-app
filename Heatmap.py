#!/usr/bin/env python
# coding: utf-8

# In[2]:


from scipy.interpolate import interp1d
import pandas as pd
import plotly.express as px
import numpy as np


# In[3]:


df = pd.read_csv('cities cases.csv')


# In[4]:


list1 = df.cases.values.tolist()


# In[5]:





# In[6]:


m = interp1d([1,max(list1)],[5,16])
circle_radius = m(list1)


# In[9]:


typelist = ['carto-darkmatter']

for i in typelist:
    print(i)
    fig = px.density_mapbox(df, lat='latitude', lon='longitude', radius=circle_radius,zoom=0,
                           mapbox_style=i)
    fig.show()


# In[ ]:




