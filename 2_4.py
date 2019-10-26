
# coding: utf-8

# In[4]:


def square(x):
    return x*x
def triple(x):
    return 3*x
def identity(x):
    return x
def incr(x):
    return x+1
def foo(f, n):
    def result(t):
        
        for i in range(0,n):
            t=f(t)
            
        return t   


    return result


add3 = foo (incr, 3)
print(add3(5))

add3 = foo (triple, 5)
print(add3(1))
print( foo(square,4)(5))

