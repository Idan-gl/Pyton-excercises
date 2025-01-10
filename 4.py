#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[9]:


def idan(max):
    max= lista[0]
    for i in lista:
        if len(i)>len(max):
            max=i
    return max

lista=["idan","gamliel","ultradata"]
print(idan(lista))


# In[ ]:




