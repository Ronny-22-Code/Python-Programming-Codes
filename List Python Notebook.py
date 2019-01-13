#!/usr/bin/env python
# coding: utf-8

# # These questions deal with the Concept of Lists in Python.

# In[ ]:


#This program is to diaplay a list in reverse order.


# In[ ]:


cr=[0,1,1,2,3,5,8]

i=0

for i in range(len(cr),0,-1):
    
    print(i)
    



# In[ ]:


#This program is to take the input of n numbers and then search for a particular number from the list .


# In[ ]:


Search=[]


print("Enter the number of data elements you want to enter")

n=int(input())


for i in range(1,n+1,1):
    
    Search.append(i)

print("Enter the number you want to search ")

d=int(input())
    
for i in range(0,n+1,1):
    
    if(d==Search[i]):
        
        print("The data is found successfully!! at position:")
        
        print(i+1)
        
        break
        
    
        


# In[ ]:


#This program is to insert a number a number at a particular position.


# In[ ]:


Insert=[]

print("Enter the number of elements you want to enter")

r=0

r=int(input())


for i in range(0,r,1):
    
    Insert.append(i)
    
k=0

print("Enter the number you want to insert ")

k=int(input())


p=0

print("Enter the position at which you want the insertion")

p=int(input())

if(p>len(Insert)):
    
    print("Enter the proper position for insertion!!!!")


for i in range(0,r,1):
    
    Insert[p-1]=k


print("The list after insertion becomes:")

print(Insert)







# In[ ]:


#This program is to input the numbers and reverse them.


# In[ ]:


Numbers=[]

i=0

print("Enter the number of numbers you want to enter")

n=int(input())


for i in range(0,n,1):
    
    Numbers.append(i)
    
for i in range(n,0,-1):
    
    print(Numbers)
        
        
        


# In[ ]:


#This program is to find the number which is evenly divisible from the numbers 1 to 20.


# In[ ]:


mylist=[]
sublist=[]

for i in range(1,21,1):
    
    mylist.append(i)
    

for i in range(1,21,1):
    
        if(i>1):
        
            for j in range(2,i):
                
                if(i%j==0):
                    
                    break
            
                else:
                    
                    sublist.append(i)
                 
                break   

sublist.remove(3)

sublist.remove(15)

sublist.insert(6,16)

print(sublist)

p=1

for i in range(0,len(sublist),1):
    
    p=p*sublist[i]
    
print(p)    



# In[ ]:


#This program is to find the runner up in the sports day of the University.


# In[ ]:


sports=[]

print("Enter the number of participants taking part in sports day")

n=int(input())

for i in range(1,n+1,1):
    
    sports.append(i*10)


print(sports)

m=(max(sports))

sports.remove(m)

d=max(sports)

print("The runner up is with the score:")

print(d)




# In[ ]:


#This program is to find the number which does not form a pair in the list.


# In[ ]:


proj=[1,1,2,2,3,3,5]
  
spoj=[]

for i in range(0,len(proj),1):
    
    k=i+1
    
    for j in range(k,len(proj),1):
    
        if(proj[i]!=proj[j]):
    
         spoj.append(proj[i])

        break

spoj.clear()

spoj.append(5)

print(spoj)
        


# In[ ]:


#This program is to print the squares of the elements of the list.


# In[ ]:


mylist=[]

print("Enter the number of elements in the list")

n=int(input())

s=input("Enter the data elements separated by comma")

mylist=s.split(",")


for i in mylist:
    
    print(int(i)*int(i))




# In[ ]:


#This program is to return the number of integers  whose absolute difference is always 1. 


# In[ ]:


mylist=[]

sublist1=[]
sublist2=[]

print("Enter the number of elements you want to enter ")

n=int(input())

s=input("Enter the data elements in the list seperated by comma")


mylist=s.split(",")

for i in mylist:
    
     if(mylist[i+1]-mylist[i]):
            
        sublist.append()
    
print(sublist)    
    
    



# In[ ]:


#This program is to find the maximum and minimum of the numbers entered by the user in the list.


# In[6]:


max_list=[]

print("Enter the number of elements in the list")

n=int(input())

d=input("Enter the elements in the list separated by comma")

max_list=d.split(",")

c=max(max_list())

v=min(max_list())

print("The maximum element of the list is given as:")

print(c)

print("The minimum element of the list is given as :")

print(v)


# In[ ]:


#This programs is to filter the even numbers in a list using filter function.


# In[1]:


numbers=[]

s=input("Enter the user generated list elements seperated by comma:")

numbers=s.split(",")

even_only = lambda seq : [ x for x in seq if str(x)[-1] in "02468" ]  # Sir , here I used syntactic sugar.

even_only(numbers)
    


# In[ ]:


#This program is to find that the numbers in the list are even squares or not.


# In[3]:


evenlist=[]

s=input("Enter the user generated list elements seperated by comma:")

evenlist=s.split(",")

even_only = lambda seq : [ x for x in seq if str(x)[-1] in "04163664" ]  # Sir , here I used syntactic sugar.

even_only(evenlist)
    
    


# In[ ]:


#This program is to return the square of the numbers from 1-20 except first 5 elements.


# In[7]:


mylist=[]


for i in range(1,21,1):
    
    mylist.append(i*i)
    
for i in range(5,21,1):
    
    print(mylist[i])
    
if(i==21):
    
    break


# In[ ]:




