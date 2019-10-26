
# coding: utf-8

# In[2]:


def checking(x):
    if(x/10>9):
        
        if(x%10<(x/10)%10 and x%10 != (x//10)%10 ):
            
            return False
    if(x/10<10 and (x%10<x/10) and (x%10 != x//10)):
        return False
    if(x//10==0):
        return True

    return checking(x//10)
print(checking(5))
print(checking(11))
print(checking(127))

