#!/usr/bin/env python
# coding: utf-8

# # These programs are based on the concepts of Files , Modules and Classes.

# In[ ]:


#This program is to define a function which will return a list without first five elements.


# In[7]:


mylist=[]

sublist=[]

def list_5(mylist):
    
    for i in mylist:
        
        sublist.append(i*i)
        
    return(sublist) 
    


for i in range(1,21,1):
    
    mylist.append(i)
    
    
list_5(mylist)    
    


# In[ ]:


#This program gives the dictionary returning the squares of the elements.


# In[1]:


d={}

for i in range(1,11,1):

    d[i]=i*i
    
print(d)    


# In[ ]:


#This programs is to filter the even numbers in a list using filter function.


# In[3]:


numbers=[]

s=input("Enter the user generated list elements seperated by comma:")

numbers=s.split(",")

even_only = lambda seq : [ x for x in seq if str(x)[-1] in "02468" ]  # Sir , here I used syntactic sugar.

even_only(numbers)
    
    


# In[ ]:


#This program is to find that the numbers in the list are even squares or not.


# In[5]:


evenlist=[]

s=input("Enter the user generated list elements seperated by comma:")

evenlist=s.split(",")

even_only = lambda seq : [ x for x in seq if str(x)[-1] in "04163664" ]  # Sir , here I used syntactic sugar.

even_only(evenlist)
    
    


# In[ ]:


#This program is to write up a module for the areas of 2d and 3d surfaces.


# In[13]:


import Temp_Module

print(Temp_Module.c_area(5))

print(Temp_Module.s_area(12))

print(Temp_Module.cube(4))

print(Temp_Module.cuboid(5,12,10))

print(Temp_Module.sphere(4))




# In[ ]:


#This program is to create an unbiased coin simulator .


# In[21]:


import random

toss=['H','T','H','T','T','H','T','H']


random.shuffle(toss,random.random)

print(toss)


# In[ ]:


#This program is to create a module where toss yields 60% heads and 40% tails.


# In[28]:


import random

TotalHeads = 0
TotalTails = 0
i = 0
Probability = int(input("Enter a probability for heads between 1 and 100: "))
NumberOfTrials = int(input("How many times do you wish to flip the coin? "))

def biasedflip():

    global TotalTails
    global TotalHeads

    if random.randint(1,100) < Probability:

        print("Heads")
        TotalHeads += 1

    else:

        print("Tails")
        TotalTails += 1

while i < NumberOfTrials:
    biasedflip()
    i += 1

print("After {0} flips there was {1} Head(s) and {2} Tail(s)".format(NumberOfTrials,TotalHeads,TotalTails))


# In[ ]:


#This program is to count the number of words in a text file.


# In[37]:


import sys
file=open(sys.argv[1],"r+")
wordcount={}
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
for key in wordcount.keys():
    print ("%s %s " %(key , wordcount[key]))

file.close()


# In[ ]:





# In[ ]:




