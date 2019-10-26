
# coding: utf-8

# In[1]:


def sum_num(n):
    if n<=0:
        return 0
    else:
        return n+sum_num(n-2)


# In[2]:


sum_num(4)

