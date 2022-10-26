#!/usr/bin/env python
# coding: utf-8

# # Escher Visualizations

# In[1]:


import escher
from escher import Builder
import cobra
from time import sleep


# In[2]:


builder = Builder(
    map_name='e_coli_core.Core metabolism',
    model_name='e_coli_core',
)
builder

