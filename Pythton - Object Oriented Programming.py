#!/usr/bin/env python
# coding: utf-8

# In[80]:


class Employee():
    def __init__ (self,name,last_name,age):
        self.name = name
        self.last_name = last_name
        self.age = age
    def __str__ (self):
        return (f"{self.name}, {self.last_name}, {self.age}")
    def __len__(self):
        return self.age
    def __del__(self):
        print ('It is deleted')


# In[81]:


x = Employee('Jack', 'Bicer', 34)


# In[82]:


x.name


# In[83]:


x.last_name


# In[84]:


x.age


# In[85]:


print(x)


# In[86]:


str(x)


# In[87]:


len(x)


# In[88]:


del(x)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




