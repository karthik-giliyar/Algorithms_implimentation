#!/usr/bin/env python
# coding: utf-8

# # Binary Search

# In[1]:


def binary_search(a,key):
    low=0
    high=len(a)-1
    found=False
    while low<=high and not found:
        mid=(low+high)//2
        if key==mid:
            found=True
        elif key<mid:
            high=mid-1
        else:
            low=mid+1
        
    if found==True:
        print("key found")
    else:
        print("key not found")
        
a=[12,3,43,5,3,4,36,78,9,67,88]
a.sort()
key=int(input("enter a num as key:  "))
binary_search(a,key)

    


# # slection sort in python: type1

# In[5]:


def find_min_index(a,next_index):
    minIndex=next_index
    next_index+=1
    while next_index<len(a):
        if a[next_index]<a[minIndex]:
            minIndex=next_index
        next_index+=1
    return minIndex   

def selection_sort(a):
    first_index=0
    while first_index<len(a):
        min_index=find_min_index(a,first_index)
        if first_index!=min_index:
            a[first_index],a[min_index]=a[min_index],a[first_index]
        first_index+=1    
        
a=[int(i) for i in input().strip().split()]
selection_sort(a)

for num in a:
    print(num,end=" ")


# # slection sort in python: type2

# In[14]:


def selection_sort(a):
    
    for i in range (len(a)):
        
        for j in range (i+1,len(a)):
            
            if a[j]<a[i]:
                
                a[i],a[j]=a[j],a[i]       
                   
a=[int(i) for i in input().strip().split()]

selection_sort(a)

for num in a:
    print(num,end=" ")


# # slection sort in python: type3

# In[15]:


def selection_sort(a):
    
    for i in range (len(a)):
        
        min_index=i
        
        for j in range (i+1,len(a)):
            
            if a[j]<a[min_index]:
                
                min_index=j
                
        a[i],a[min_index]=a[min_index],a[i]              
                   
a=[int(i) for i in input().strip().split()]

selection_sort(a)

for num in a:
    print(num,end=" ")


# # buuble sort

# In[22]:


def bubble_sort(a):
    for i in range (len(a)):
        for j in range (len(a)-1-i):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                
a=[int(i) for i in input().strip().split()]
bubble_sort(a)

print(a)                    # output as a list

for num in a:
    print(num,end=" ")      # output in the form of spaced numbers


# # insertion sort

# In[5]:


def insertion_sort(a):
    for i in range (1,len(a)):
        j=i-1
        while j>=0 and a[j+1]<a[j]:
            a[j],a[j+1]=a[j+1],a[j]
            j-=1    

a=[int(i) for i in input().strip().split()]
insertion_sort(a)
print(a)


# # merge sort

# In[7]:


def merge_sort(a):
    if len(a)>1:
        mid=len(a)//2
        left_sub=a[:mid]
        right_sub=a[mid:]
        merge_sort(left_sub)
        merge_sort(right_sub)
        
        i,j,k=0,0,0
        while i<len(left_sub) and j<len(right_sub):
            if left_sub[i]<right_sub[j]:
                a[k]=left_sub[i]
                k+=1
                i+=1
            else:
                a[k]=right_sub[j]
                k+=1
                j+=1
                
        while i<len(left_sub):
            a[k]=left_sub[i]
            i+=1
            k+=1
        while j<len(right_sub):
            a[k]=right_sub[j]
            j+=1
            k+=1
        
a=[int(i) for i in input().strip().split()]
merge_sort(a)
print(a)


# # quick sort

# In[11]:


def pivot_place(a,first,last):
    pivot=a[first]
    left=first+1
    right=last
    while True:
        while left<=right and a[left]<=pivot:
            left+=1
        while left<=right and a[right]>=pivot:
            right-=1
        if left>right:
            break
        else:
            a[left],a[right]=a[right],a[left]
    a[first],a[right]=a[right],a[first]
    return right

def quicksort(a,first,last):
    if first<last:
        p=pivot_place(a,first,last)
        quicksort(a,first,p-1)
        quicksort(a,p+1,last)
        
a=[int(i)for i in input().strip().split()]
first_index=0
last_index=len(a)-1
quicksort(a,first,last)
print(a)

