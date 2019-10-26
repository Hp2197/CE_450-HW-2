
# coding: utf-8

# In[1]:


def square(x):
    return x*x
def triple(b):
    return 3*b
def increment(x):
    return x+1
def identity(x):
    return x
def intscts(f,x):
    def g(a):
        if f(x)==a(x):
            return True
        else:
            return False
    return g


# In[2]:


at_3=intscts(square,3)


# In[3]:


at_3(triple)

