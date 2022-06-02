#!/usr/bin/env python
# coding: utf-8

# In[5]:


a = int(input("1-Sonni kiriting:  "))
b = input("Amalni tanlang: |(+, -, *, / )|  ")
c = int(input("2-Sonni kiriting:  "))
k = True

if b == "+":
    a = a + c
elif b == "-":
    a = a - c    
elif b == "*":
    a = a * c    
elif b == "/":
    a = a / c    
else:
    k = False
    
if k:
    print("Natija:", a)
else:
    print("Nimadir xato ketdi...")
    


# In[ ]:




