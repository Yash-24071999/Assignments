#!/usr/bin/env python
# coding: utf-8

# In[48]:


import pandas as pd
import scipy.stats as s
import numpy as np


# In[40]:


data = pd.read_csv('data.csv')


# In[41]:


data.head()


# In[42]:


data.drop(labels=[data.columns[0],data.columns[32]],axis=1,inplace=True)


# In[43]:


data.head()


# In[44]:


diagnosis_unique_value = data['diagnosis'].unique()


# In[45]:


radius_mean_unique_value = data['radius_mean'].unique()


# In[75]:


def determine_random_variable_type(column_name):
    if (type(data[column_name][0]) == str or type(data[column_name][0]) == int) and (len(data[column_name].unique()) < len(data[column_name])):
        return 'discrete'
    else:
        return 'continous'


# In[76]:


type(data['diagnosis'][2])


# In[77]:


determine_random_variable_type('diagnosis')


# In[49]:


def calculate_L_max_normal(column_name):
    mu_best_normal = data[column_name].mean()
    sigma_best_normal = data[column_name].std()
    L_max_normal = np.sum(s.norm.logpdf(mu_best_normal,sigma_best_normal))
    return L_max_normal


# In[50]:


def calculate_L_max_rayleigh(column_name):
    sigma_best_rayleigh = np.sqrt(np.mean(data[column_name]**2)/2)
    L_max_rayleigh = np.sum(s.rayleigh.logpdf(data[column_name],scale=sigma_best_rayleigh)) 
    return L_max_rayleigh


# In[58]:


def determine_distribution_type(column_name):
    column_type = determine_random_variable_type(column_name)
    if column_type == 'discrete':
        if len(data[column_name].unique()) == 2:
            return 'binomial'
        else:
            return 'multinomial'
    else:
        L_max_normal = calculate_L_max_normal(column_name) 
        L_max_rayleigh = calculate_L_max_rayleigh(column_name)
        if L_max_normal > L_max_rayleigh:
             return 'normal'
        else:
            return 'rayleigh'


# In[78]:


determine_distribution_type("diagnosis")

