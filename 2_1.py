
# coding: utf-8

# In[4]:


def fancy_printing(n):

    
    a=[]
    for i in range(1,n+1):
        if(n%i==0):
            a.append(i)
            
    def result(n):
        b=[]
        t=0
        
        for i in range(0,n+1):
            b.append(i)
        for i in range(0,len(a)):
            
            while(t<len(b)-1):
                if(a[i]==b[t]):
                    b[t]="buzz!"
                    break
                t+=1
        i=0
        while(i<len(b)):

            print(b[i])
            i+=1
    return result

replace = fancy_printing (18)
replace(20)

