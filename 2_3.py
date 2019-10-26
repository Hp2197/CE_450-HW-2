
# coding: utf-8

# In[1]:


a=0
def is_prime(n):
  def helper(i):
    if i==1:
      return True
    elif i==0:
      return False
    elif n%i==0:
      return False  
    return helper(i-1)
  return helper(n-1)
def cnt_primes(m):
  global a
  if(is_prime(m)):
    a+=1
  if m<2:
    b=a
    a=0
    return b
  else:
    return cnt_primes(m-1)


# In[3]:


cnt_primes(4)

