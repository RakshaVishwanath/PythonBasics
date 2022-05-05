#!/usr/bin/env python
# coding: utf-8

# In[1]:


list = [1,2,3,'raksha']
print(list)


# In[2]:


# append(), extend(), and insert()
list.append(4)
print(list)


# In[3]:


list.append((5,6))
print(list)


# In[8]:


list.extend((5,6))
print(list)


# In[9]:


# difference between append and extend is append adds a tuple, whereas extend adds single element
print(list)
list.insert(0,10)
print(list)
#Insert adds the second parameter as the element in the index mentioned in first parameter


# In[11]:


# del, pop(), remove()
del list[0]
print(list)


# In[12]:


list.pop(2)
print(list)


# In[13]:


a=list.pop(2)
print(a)


# In[14]:


list.remove(3)
print(list)


# In[15]:


# remove removes the element specified inside the bracket
list.remove('raksha')
print(list)


# In[16]:


print(list[:])
print(list[2:4])
print(list[::-1])
print(list[0:4:2])


# In[18]:


#difference between sorted and sort
list1=[4,10,0,6,3,90,10,105,67]
print(sorted(list1))
print(list1)


# In[19]:


list1.sort(reverse=True)
print(list1)


# In[21]:


list1.sort()


# In[22]:


print(list1)


# In[23]:


print(list1.index(6))
print(list1.count(10))


# In[24]:


#tuple
tuple= (1,2,3)
print(tuple)


# In[27]:


tuple1=tuple+(4,5,6)
print(tuple1)


# In[28]:


tuple[1]=2
print(tuple)


# In[31]:


l=[1,2,3]
l[2]=4
print(l)


# In[42]:


###Dictionary

dict1={1:"Raksha",2:"Bhadra"}
print(dict1)


# In[43]:


dict1[2]="abc"
print(dict1)


# In[44]:


dict1[3]="xyz"
print(dict1)


# In[45]:


del dict1[3]
print(dict1)


# In[46]:


a=dict1.pop(1) #pop removes the element that is specified
print(a)
print(dict1)


# In[47]:


print(dict1.popitem()) # the value that is at the last is removed


# In[51]:


dict2={1:"a",2:"b",3:"c"}
print(dict2.keys())


# In[52]:


print(dict2.values())


# In[53]:


print(dict2.items())


# In[54]:


### sets  
##unordered collection of unique elements
## sets are mutable

set1={1,2,3,4,4,4}
print(set1)  # it prints only one time


# In[56]:


set1.add(5)
print(set1)


# In[57]:


#union(), intersection(), difference(), symmetric_difference()

set2={5,6,7,8,9}
print(set1.union(set2))


# In[58]:


print(set1.intersection(set2))


# In[59]:


print(set1.difference(set2))


# In[61]:


print(set1.symmetric_difference(set2))  # removes only the common elements and gives the elements of both the sets 


# In[69]:


### user defined data structures
# Stack
# Queues
# Hashmaps
# trees
# graphs 
# linked lists

# The difference between the array and the list is that array can have only store one type of data whereas list can store multiple datatypes

import array as arr
a=arr.array('i',[1,2,3,4,5])
print(a)
for i in a:
    print(i)


# In[70]:


a.append(7)
for i in a:
    print(i)


# In[71]:


a.pop(3)
for i in a:
    print(i)


# In[76]:


# # Stacks
# Stacks are made from arrays
# stack follow last in first out (LIFO)
# They have pointer called top to take care of top of the element
stack=[]
stack.append("a")
stack.append("b")
stack.append("c")
print(stack)


# In[77]:


a=stack.pop()
b=stack.pop()
c=stack.pop()
print(a,b,c)


# In[78]:


stack.pop()
print(stack)


# In[82]:


# ### Queue 
# Queue follows FIFO priniciple that is first in first out 
from collections import deque
q= deque()
q.append("r")
q.append("a")
q.append("k")
print(q)


# In[83]:


a=q.popleft()
b=q.popleft()
c=q.popleft()
print(a,b,c)


# In[ ]:


# Trees- used to define hierarchy


# In[ ]:




