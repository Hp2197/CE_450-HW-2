
# coding: utf-8

# In[2]:


def cal(n):
    if n < 0:
        return 1
    else:
        return n*cal(n-2)


# In[3]:


cal(5)

