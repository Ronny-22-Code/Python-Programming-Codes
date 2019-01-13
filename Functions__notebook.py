#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#These programs are coded using functions in python.


# In[ ]:


#This program is to return x raised to the power y.


# In[ ]:


def rp(x,y):
    
    return(pow(x,y))

 
print("Enter the value of the base:")

a=int(input())
    
print("Enter the value of the mantissa:")

b=int(input())
    
rp(a,b)    
    
    
    
    
    
    


# In[ ]:


#This program is to concatenate the two strings and return the concatenated.


# In[ ]:


def con(x='Hello', y='World'):
    
    return(x+y)

print("Enter the first string:")

c=str(input())

print("Enter the second string:")

d=str(input())

con(c,d)
    
    
    





# In[ ]:


#This program is to return a bool value if a number is even or not.


# In[ ]:


def boo(x):
    
    if(x%2==0):
        
        return True
    
    else:
        
        return False
    
print("Enter the value")

n=int(input())

boo(n)



# In[ ]:


#This program is to return a bool value if the number is prime or not.


# In[ ]:


def priboo(x):
    
    for i in range(2,x,1):
        
        if(x%i==0):
            
            return False
        else:
            
            return True


print("Enter any number to check")

n=int(input())

priboo(n)
        
        
        
        
        
        
        
        
        
        
        
        


# In[ ]:


#This program is to return a boolean value if the number is a palindrome.


# In[3]:


def palboo(x):
    
    b=x
    
    r=0
    
    d=x%10
    
    r=r+d
    
    x=x//10
    
    if(b==r):
        
        return True
        
    else:
        
        return False
    
    
print("Enter anything")

a=int(input())


palboo(a)    











# In[ ]:


#This program is to count the number of words in the string.


# In[10]:


def wordcount(x):
    
    l=0
    
    k=0
    
    l=len(x)
    
    for i in  range(1,l,1):
        
        if(i==' '):
            
            k=k+1
            
        print(k)
        
        break

   

        
print("Enter the string:")

c=str(input())

wordcount(c)


# In[ ]:





# In[ ]:




