
# coding: utf-8

# In[1]:


i=1
def operation(a,b,c):
    global i
    if i > b:
        i=1
        return c
    else:
        i+=1
        return operation(a,b,c+a)


# In[2]:


operation(2,4,3)

