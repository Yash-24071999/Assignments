#!/usr/bin/env python
# coding: utf-8

# In[28]:


import numpy as np
random_integers=np.random.randint(low=0,high=2000,size=(1000,))


# In[29]:


def is_prime(num,divisor):
    if num==1 or num==2:
        return True
    else:
        if divisor==num:
            return True
        if num%divisor==0:
            return False
        bool_value=is_prime(num,divisor+1)
    return bool_value


# In[30]:


is_prime(61,2)


# In[31]:


def even_prime_list_creation(all_number,even,prime):
    if len(all_number)==0:
        return prime,even
    if all_number[0]%2==0:
        even.append(all_number[0])
    else:
        if is_prime(all_number[0],2)==True:
            prime.append(all_number[0])
    all_num.pop(0)
    prime_lst,even_lst=even_prime_list_creation(all_number,even,prime)
    return prime_lst,even_lst
    


# In[32]:


all_num=list(random_integers)
even_num=[]
prime_num=[]


# In[33]:


p_list,e_list=even_prime_list_creation(all_num,even_num,prime_num)

