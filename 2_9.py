
# coding: utf-8

# In[1]:


def A(n):
    if n <= 3:
        return n
    else:
        return A(n-1)+2*A(n-2)+3*A(n-3)


# In[2]:


A(1)

