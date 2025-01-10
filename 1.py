#!/usr/bin/env python
# coding: utf-8

# In[12]:


adress = input("Do you live in Rotchild st in Tel Aviv?[yes/no]")
if adress == "no":
    print("Go Home")

age= int(input("How old are you?")) 
if age>=24:
     print("Ggreat")
elif  age == 23: 
    bday = input("Do you have bday today?[yes/No]")
    if age == 23 and bday == "yes":
         print("Ggreat") 
    if age == 23 and bday == "no":
        print("Go Home")
elif age < 23:
    print("Go Home")


# In[ ]:




