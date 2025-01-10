#!/usr/bin/env python
# coding: utf-8

# In[38]:


a=str(input("Choose a word"))

if len(a)<3:
    a=a
if len(a)>3:
    b=a[-3]+a[-2]+a[-1]
    if len(a)>3 and b!="abc": 
        a=a+"abc"
    if len(a)>3 and b=="abc":
        a=a+"qwd"
print(a)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




