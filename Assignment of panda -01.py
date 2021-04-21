#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd


# In[9]:


df = pd.read_csv("train.csv")


# In[3]:


df


# # First probability

# \begin{equation}
# P(target = 0 | (1 <= var_0 <= 15) \cap (-10 <= var_1 <= 9.5) \cap (4 <= var_2 <= 18))
# \end{equation}

# In[5]:


boolean_first = df['target'] == 0


# In[31]:


first_num = df[boolean_first].shape[0]


# In[32]:


first_num


# In[28]:


boolean_sec =(df["var_0"] >=1) & (df['var_0'] <= 15) & (df['var_1'] >= -10) & (df['var_1'] <= 9.5) & (df['var_2'] >= 4) & (df['var_2'] <= 18)


# In[37]:


first_deno = df[boolean_sec].shape[0]


# In[38]:


first_deno


# In[34]:


first_probability = first_num/first_deno


# In[35]:


first_probability


# \begin{equation}
# P(target = 0 | (1 <= var_0 <= 15) \cap (-10 <= var_1 <= 9.5) \cap (4 <= var_2 <= 18)) = 0.9930503806006812
# \end{equation}

# # Second Probability

# \begin{equation}
# P((1 <= var_0 <= 15) \cap (-10 <= var_1 <= 9.5) \cap (4 <= var_2 <= 18) | target=0)
# \end{equation}

# In[39]:


sec_num = first_deno


# In[41]:


sec_deno = first_num


# In[42]:


second_probability = sec_num/sec_deno


# In[43]:


second_probability


# \begin{equation}
# P((1 <= var_0 <= 15) \cap (-10 <= var_1 <= 9.5) \cap (4 <= var_2 <= 18) | target=0) = 1.0069982546052851
# \end{equation}

# # Third Probability

# \begin{equation}
# P(target=1 | (1 <= var_0 <= 15) \cap (-10 <= var_1 <= 9.5) \cap (4 <= var_2 <= 18))
# \end{equation}

# In[44]:


boolean_third = df['target'] == 1


# In[45]:


third_num = df[boolean_third].shape[0]


# In[46]:


third_num


# In[47]:


third_deno = first_deno


# In[48]:


third_deno


# In[49]:


third_probability = third_num/third_deno


# In[50]:


third_probability


# \begin{equation}
# P(target=1 | (1 <= var_0 <= 15) \cap (-10 <= var_1 <= 9.5) \cap (4 <= var_2 <= 18)) = 0.1109399926032645
# \end{equation}

# # Fourth Probability

# \begin{equation}
# P((1 <= var_0 <= 15) \cap (-10 <= var_1 <= 9.5) \cap (4 <= var_2 <= 18) | target=1)
# \end{equation}

# In[55]:


fourth_num = third_deno


# In[52]:


fourth_deno = third_num


# In[53]:


fourth_probability = fourth_num/fourth_deno


# In[54]:


fourth_probability


# \begin{equation}
# P((1 <= var_0 <= 15) \cap (-10 <= var_1 <= 9.5) \cap (4 <= var_2 <= 18) | target=1) = 9.0138819783063
# \end{equation}
