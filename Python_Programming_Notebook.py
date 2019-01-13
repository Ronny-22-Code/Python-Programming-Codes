#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# This program is to Swap Two Variables.


# In[ ]:


x=3
y=5

x=x+y
y=x-y
x=x-y

print("The Swapped Variables are:")
print(x,y)


# In[ ]:


# This program is to Print the natural numbers from 1 to n and then print it in the reverse order.


# In[ ]:


n=int(input())

for i in range(1,n):
    
    print(i)
    
for i in range(n,1):
    
    print(i)
    
    
    


# In[ ]:


# This program is to print the Volume of the Sphere.


# In[ ]:


print("Enter the radius of the sphere")

r=int(input())

v=((4*3.14)/3)*(pow(r,3))

print("The volume of the Sphere is:")

print(v)


# In[ ]:


# This program is to print all the odd numbers and even numbers between 1 and 100.


# In[ ]:


print("The required output is :")

print("The Odd  Numbers are:")

for i in range(1,100,1):
    
    if(i%2!= 0):
    
        print(i)
    
print("The Even Numbers are:")
    
for i in range(1,100,1):
    
    if(i%2==0):
    
        print(i)
    
    
    
    
    
    
    


# In[ ]:


# This program is to count the number of digits in a Number.


# In[ ]:


print("Enter the digit")

r=int(input())

k=0

while(r>0):
    
    r=r//10
    k=k+1
    
print("The number of digits are:")

print(k)    
    
    
    



# In[ ]:


# This program is to check whether the number is prime or not.


# In[ ]:


print("Enter the number:")

n=int(input())

for i in range(2,n,1):
    
    if(n%i==0):
        
        print("The number is not a Prime Number")
        
        break
    
    else:
        
        print("The number is a Prime Number")

        break





# In[ ]:


# This program is to Sum of the numbers where only the multiples of 3 and 5 are considered. 


# In[ ]:


print("Enter the number upto which sum is to be calculated ")

n=int(input())

s=0

for i in range(1,n,1):
    
    if(i%3==0) or (i%5==0):
        
        s=s+i        

print("The sum of the numbers is:")

print(s)







# In[ ]:


#This program is to Provide the user an option to compute the Sum or Product.


# In[ ]:


print("Enter the number")

n=int(input()) 

print("Enter 1 for the sum or enter 0 for the product of the numbers")

d=int(input())

s=0

p=1

if(d==1):
    
    for i in range(1,n,1):
        
        s=s+i
        
        print(s)   

elif(d==0):
    
    for i in range(1,n,1):
        
        p=p*i
    
        print(p)
else:
    
    print("Enter a valid choice")
    
    
    
    
    




# In[ ]:


# This program is to sum up the multiples of 3 and 5.


# In[ ]:


print("The Sum will be :")

s=0

for i in range(1,1000,1):
    
    if(i%3==0) or (i%5==0):
        
        s=s+i
        
    else:
        
        s=0
        
print(s)        
        


# In[ ]:


#This program is to print those numbers which are divisible by 7 and are multiple of 5.


# In[ ]:


print("Those numbers are:")


for i in range(2000,3201,1):
    
    
    if(i%7==0) or (i%5!=0):
        
        print(i)
        
        
        
        
    


# In[ ]:


# This program is to find the difference between the squares of the sum of the one hundred natural numbers and their Sum.


# In[ ]:


print("The output will be:")

s=0

d=0

k=0


for i in range(1,100,1):
    
    s=s+i
    
for i in range(1,100,1):
    
    k=k+i*i
    
    
d=k-s

print(d)



    









# In[ ]:


#This program is to the average , sum and count for n numbers.


# In[ ]:


s=0

k=0

f=0

i=0    

c=str(input("Enter Stop to terminate:"))


while(c):    
        
    s=s+i
    
    k=k+1
    
    f=s/k

    i=i+1
    
    
     
    print(s)
    
    print(k)
    
    print(f)
    
    




    
        







# In[ ]:


#This program is to print all the prime numbers uptill n.


# In[1]:


x = int(input("Enter the number:"))

k=1

for i in range (1, x, 1):
    
    c=0
    
    for j in range (1, k+1, 1):
        
        if((k%j)==0):
        
            c = c+1

    if (c==2):
          
            print (k)
    
    else:
          i = i-1

    k=k+1


    
    
    
        
        
        
        
    




# In[ ]:


#This program is to compute the factorial of a number.


# In[ ]:


print("Enter the number of which the factorial is to be calculated")

n=int(input())

if(n>0):

    f=1

for i in range(1,n,1):
    
    f=f*i
    
f=f*n

print(f)


# In[ ]:


# This program is to print the fibonacci series.


# In[ ]:


print("Enter the number upto which the Fibonacci series is to be printed")

n=int(input())

a=0
b=1

s=0

print(a)

print(b)

c=2

while(c<n):
        
    s=a+b
        
    c=c+1
        
    print(s)
        
    a=b  
    b=s
        
        
        
    
        
    



# In[ ]:


#This program is to calculate the LCM of the two numbers.


# In[ ]:


print("Enter the two numbers for which LCM is to be calculated:")

a=int(input())

b=int(input())

m=0

if(a>b):
    
    m=a
    
else:
    
    m=b


while(1):
    
    if((m%a==0)and(m%b==0)):
        
        print("The LCM of the two numbers" ,a,b,"is",m)
        
        break    
    
        m=m+1
        
    else:
        
        m=a*b
        




# In[ ]:


#This program is to find the factors of a number.


# In[1]:


print("Enter the number whose factors is to be calculated")

n=int(input())

for i in range(2,n,1):
    
    if(n%i==0):
        
        print(i)








# In[ ]:


#This program is to compute the value of a+aa+aaa+aaaa.


# In[ ]:


print("Enter the value of the integer a ")

a=int(input())

k=0

f=0

d=0

s=0

d=a*10+a

f=a*100+d

k=a*1000+f

s=a+f+d+k

print("The required output is:")

print(s)








# In[ ]:


###Strings###


# In[ ]:


#This program is to find the length of the string.


# In[ ]:


print("Enter the String of which length is to be calculated ")

c=str(input())

k=0

for letter in c:
    
    
    k=k+1

print(k)    






# In[ ]:


#This program is to calculate the number of letters and digits.


# In[ ]:


print("Enter any sentence")


c=str(input())

i=' '

k=0

l=0

for i  in c:
    
    if(i.isalpha()):
    
        k=k+1
    
    else:
        
        l=l+1
    

        

    
print(k)

print(l)






# In[ ]:


#This program is to Count the number of uppercase and lowercase letters.


# In[ ]:


print("Enter the Sentence")

c=str(input())

i=' '

k=0

m=0

for i in c:
    
    if(i.isupper()):
        
        k=k+1

    else:
        
        m=m+1
        

print(k)

print(m)


# In[ ]:


# This program is to perform Swap Cases in a string.


# In[ ]:


print("Enter the string:")

c=str(input())

print(c.swapcase())




# In[ ]:


# This program is to count the occurences of letters.


# In[ ]:


c = "Hello"

k = c.count('o')

print(k)



# In[ ]:


#This program is to check whether the string is a palindrome or not.


# In[2]:


print("Enter the string:")

c=str(input())

d=c[::-1]

if(c==d):
    
    print("The string is a palindrome")
    
else:
    
    print("The string is not a palindrome")



# In[ ]:


#This program is to check the number of occurences of a substring.


# In[1]:


print("Enter the string:")

c=str(input())

print("Enter the substring you want to search")

h=str(input())

k=0

k=c.count(h)

print(k)


# In[ ]:


#This program is to reverse a string.


# In[3]:


print("Enter the string:")

c=str(input())

print(c[::-1])



# In[ ]:


#This program is to check the number oc consecutive 1 in a binary number.


# In[4]:


c= 0
m= 0
for i in str(input()):
    if (i == '1'):
        c=c+1
    elif(c > m):
        m = c
        c = 0
    else:
        c = 0

print(c)    



# In[ ]:


#This program is to find the non repeated number in a string.


# In[7]:


print("Enter the string")

c=str(input())

for i in c:
        
    for j in c:
        
        if(j!=i):
            
            k=j

print(k)            
                
        
        






# In[ ]:


#This program is to check a substring.


# In[10]:



print("Enter the string:")

c=str(input())

print("Enter the substring you want to search")

h=str(input())

k=0

if(c.count(h)):
    
    k=k+2
    
if(k>=1):
    
    print("The sub-string exists in the string:")
    
    print(k,"times")


# In[ ]:


#This program is to check the validity of a password.


# In[15]:


print("Enter your username")

c=str(input())

print("Enter your password")

s=str(input())

for i in s:
    
    if(i.islower() and i.isdigit()and i.isupper() and len(s)>=6 and len(s)<=12):
        
        print("Your password is valid and set successfully!!!")
        
        break
        
else:
        
    print("Your Password is invalid , please try again!!!")






# In[ ]:




