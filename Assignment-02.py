#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def check_aadhar_number(string):
    if len(string)==12:
        if string.isnumeric()==True:
            return True
        elif string.isalnum()==True:
            return False
    else:
        return False


# In[ ]:


def check_pan_number(string):
    if len(string)==10:
        if string[0:5].isalpha()==True and string[5:9].isnumeric()==True and string[9].isalpha()==True:
            return True
        else:
            return False
    else:
        return False


# In[ ]:


def check_DL_number(string):
    if len(string)==15:
        if string[0:2].isalpha()==True and string[2:15].isnumeric()==True:
            return True
        else:
            return False
    else:
        return False


# In[ ]:


def check_GST_number(string):
    if len(string)==15:
        if string[0:2].isnumeric()==True and check_pan_number(string[2:12])==True and string[12].isnumeric()==True and string[13].isalpha()==True and string[14].isnumeric()==True:
            return True
        else:
            return False
    else:
        return False
        


# In[ ]:


string=str()
string=input('Enter the number: ')
if check_aadhar_number(string)==True:
    print('The {} number is Aadhar Number'.format(string))
elif check_pan_number(string)==True:
    print('The {} number is PAN Number'.format(string))
elif check_DL_number(string)==True:
    print('The {} number is DL Number'.format(string))
elif check_GST_number(string)==True:
    print('The {} number is GST Number'.format(string))
else:
    print('The {} number is default please check again!'.format(string))


# In[ ]:




