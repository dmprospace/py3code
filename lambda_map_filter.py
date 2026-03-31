# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 00:12:44 2020

@author: z093920
"""
from pprint import pprint
from functools import reduce

##################################################################################
# Lambda
#  - Way to write Simple 1 Line Function
#  - Does not use def or Return Keywords (implicit)
#  - Can be assigned to a variable (function valriable)

f=lambda x:x**2  # Read as Lambda of x = x**2 ; and named as f
y=f(2)
print(y)    # 4
##################################################################################
def multiply(i):
    return (i*i)
def add(i):
    return (i+i)
#Instead of a list of inputs we can even have a list of functions!
I=lambda x:x
J=lambda x:x*x
K=lambda x:x+x
for i in range(0,6,1):
    valuei = list(map(lambda H: H(j), [I, J, K]))
    print(valuei, end="  ")  # [0, 0, 0]  [1, 1, 2]  [2, 4, 4]  [3, 9, 6]  [4, 16, 8]  [5, 25, 10]  

print("\n")
value1 = list(map(I , [0,1,2,3,4,5]));print(value1) # [0, 1, 2, 3,  4,  5]
value2 = list(map(J , [0,1,2,3,4,5]));print(value2) # [0, 1, 4, 9, 16, 25]
value3 = list(map(K , [0,1,2,3,4,5]));print(value3) # [0, 2, 4, 6,  8, 10]

##################################################################################
#  Map
#  - Way to CALL a (lambda or normal) function for each element of an iterable and COLLECT results
#  - Map function Returns PROCESSED Iterable (by applying function on each original element) as a map_object

lst = [1,2,3,4,5,6]   # List
map_obj=map(f, lst)
pprint(list(map_obj))  # [1, 4, 9, 16, 25, 36]

st  = set([1,10,100]) # Set
map_obj=map(f, st)
pprint(set(map_obj))  # {10000, 1, 100}

dct = {1:'A', 2:'B', 3:'C'}  # Dictionary
map_obj=map(f, dct)
pprint(list(map_obj))  # [1, 4, 9]

tpl = (1,2,3,4)         # Tuple
map_obj=map(f, tpl)
pprint(tuple(map_obj))  # (1, 4, 9, 16)

##################################################################################
#  Filter
#  - Filter Items from an iterable based on (logical / boolean) CONDITION evaluated on each element, by using a (lambda or normal) function
#  - Returns modified iterable as filter_object

def f(x):
    if(x<=3):
        return True
    return False
# or
g=lambda x: x<=3

filter_obj=filter(g,lst)
pprint(list(filter_obj))         # [1, 2, 3]

##################################################################################
#  Reduce
#  - Applies same operation to items of an iterable
#    (For performing some computation on a list and returning the result. It applies a rolling computation to sequential pairs of values in a list)
#  - Uses results of one operation as first param of next operation
#  - Retun an item, not a list

h=lambda x,y:x+y
element=reduce(h,lst)
pprint(element)     # 21

