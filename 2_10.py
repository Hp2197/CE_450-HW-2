
# coding: utf-8

# In[ ]:


def bnc_bck_frth(k):
  m,n,i,a=0,1,1,1
  while(a<=k):
    m+=n
    if (a%7==0)+(a%10==7):
      if i==1:
        n=-1
        i=0
      else:
        n=1
        i=1    
    a+=1
  return m


# In[ ]:


bnc_bck_frth(7)

