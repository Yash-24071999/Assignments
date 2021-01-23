#!/usr/bin/env python
# coding: utf-8

# In[5]:


lis = [25,36,31,17,61,19,58,39,67,81]
even = list()
prime = list()
final_answer = dict()
for i in range(0,10):
    if lis[i] % 2 == 0:
        even.append(lis[i])   
    for divisor in range(2,lis[i]):
        if lis[i] % divisor == 0:
            break
    if divisor == (lis[i]-1):
        prime.append(lis[i])
final_answer["Even"]=even
final_answer["Prime"]=prime
print(final_answer)

